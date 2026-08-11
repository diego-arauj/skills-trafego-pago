#!/usr/bin/env python3
"""
Aplica configuracoes que o create.py nao cobre numa campanha de Search:
- desliga Parceiros de Pesquisa (so Google Search)
- segmentacao geografica por PRESENCA (nao interesse)
- lista de estados (geo target constants)
- idioma

Uso:
  GRPC_DNS_RESOLVER=native python3 set_campaign_settings.py \
     --customer-id 1234567890 --campaign-id 123 \
     --geo 20100,20088,20093,21230,20089,20090 --language 1014
"""
import argparse
import sys
from google.api_core import protobuf_helpers
from lib import init_client, resolve_customer_id, handle_google_error_decorator, print_json


@handle_google_error_decorator
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--customer-id", required=True)
    ap.add_argument("--campaign-id", required=True)
    ap.add_argument("--geo", required=True, help="geo target constant ids, virgula")
    ap.add_argument("--language", default="1014")
    ap.add_argument("--maxclicks-ceiling", dest="maxclicks_ceiling",
                    help="Liga Maximizar Cliques (target_spend) com teto de CPC em reais (ex: 2.00)")
    args = ap.parse_args()

    client = init_client()
    customer_id = resolve_customer_id(args.customer_id)
    campaign_service = client.get_service("CampaignService")
    crit_service = client.get_service("CampaignCriterionService")
    campaign_rn = campaign_service.campaign_path(customer_id, args.campaign_id)

    # 1. Campaign update: partners off + presenca
    op = client.get_type("CampaignOperation")
    camp = op.update
    camp.resource_name = campaign_rn
    camp.network_settings.target_google_search = True
    camp.network_settings.target_search_network = False
    camp.network_settings.target_content_network = False
    camp.geo_target_type_setting.positive_geo_target_type = (
        client.enums.PositiveGeoTargetTypeEnum.PRESENCE
    )
    camp.geo_target_type_setting.negative_geo_target_type = (
        client.enums.NegativeGeoTargetTypeEnum.PRESENCE
    )
    if args.maxclicks_ceiling:
        # Maximizar Cliques (TARGET_SPEND) com teto de CPC — correto p/ conta fria sem conversao
        camp.target_spend.cpc_bid_ceiling_micros = int(float(args.maxclicks_ceiling) * 1_000_000)
    client.copy_from(
        op.update_mask,
        protobuf_helpers.field_mask(None, camp._pb),
    )
    # GOTCHA protobuf: setar booleano p/ False NAO entra no field_mask automatico.
    # Forcar os paths de rede explicitamente, senao Parceiros de Pesquisa fica ON.
    op.update_mask.paths.append("network_settings.target_search_network")
    op.update_mask.paths.append("network_settings.target_content_network")
    campaign_service.mutate_campaigns(customer_id=customer_id, operations=[op])

    # 2. Criteria: geo (presenca) + idioma
    ops = []
    for gid in [g.strip() for g in args.geo.split(",") if g.strip()]:
        cop = client.get_type("CampaignCriterionOperation")
        c = cop.create
        c.campaign = campaign_rn
        c.location.geo_target_constant = f"geoTargetConstants/{gid}"
        ops.append(cop)
    lop = client.get_type("CampaignCriterionOperation")
    lc = lop.create
    lc.campaign = campaign_rn
    lc.language.language_constant = f"languageConstants/{args.language}"
    ops.append(lop)

    resp = crit_service.mutate_campaign_criteria(customer_id=customer_id, operations=ops)
    print_json({
        "status": "settings_applied",
        "partners": "OFF",
        "geo_type": "PRESENCE",
        "criteria_added": len(resp.results),
    })


if __name__ == "__main__":
    main()
