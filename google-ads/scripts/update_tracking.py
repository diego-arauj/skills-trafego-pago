#!/usr/bin/env python3
"""
Google Ads ClaudePRO - Rastreamento (UTM)

Le e edita o que define a UTM de uma conta:
  - campaign-params : url_custom_parameters da campanha ({_origem}, {_midia}, {_campanha}, {_anuncio})
  - ad-final-url    : final_urls de um anuncio (para tirar UTM escrita na mao da URL)

Por padrao roda em DRY-RUN. So escreve com --apply.

Exemplos:
  read:   update_tracking.py show --customer-id 1234567890
  dry:    update_tracking.py campaign-params --customer-id 1234567890 --campaign-id 987654321 --set campanha=pmax-remarketing
  apply:  update_tracking.py campaign-params --customer-id 1234567890 --campaign-id 987654321 --set campanha=pmax-remarketing --apply
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import (
    init_client,
    resolve_customer_id,
    run_query,
    print_json,
    print_error,
    handle_google_error_decorator,
    add_customer_arg,
)


def _params_to_dict(params):
    return {p.get("key"): p.get("value") for p in (params or [])}


# ---------------------------------------------------------------------------
# show
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_show(args):
    """Mostra o rastreamento atual: template + parametros por campanha, e UTM em URL de anuncio."""
    cid = resolve_customer_id(args.customer_id)

    q = """SELECT campaign.id, campaign.name, campaign.status, campaign.advertising_channel_type,
           campaign.tracking_url_template, campaign.final_url_suffix, campaign.url_custom_parameters
           FROM campaign WHERE campaign.status='ENABLED' ORDER BY campaign.name"""
    campanhas = []
    for r in run_query(cid, q):
        c = r.get("campaign", {})
        campanhas.append({
            "id": c.get("id"),
            "nome": c.get("name"),
            "tipo": c.get("advertising_channel_type"),
            "tracking_url_template": c.get("tracking_url_template"),
            "final_url_suffix": c.get("final_url_suffix"),
            "custom_params": _params_to_dict(c.get("url_custom_parameters")),
        })

    q2 = """SELECT campaign.id, campaign.name, ad_group_ad.ad.id, ad_group_ad.ad.final_urls,
            ad_group_ad.ad.tracking_url_template, ad_group_ad.ad.url_custom_parameters
            FROM ad_group_ad WHERE ad_group_ad.status='ENABLED' AND campaign.status='ENABLED'"""
    anuncios = []
    for r in run_query(cid, q2):
        a = r.get("ad_group_ad", {}).get("ad", {})
        urls = a.get("final_urls") or []
        if any("utm_" in str(u) for u in urls) or a.get("tracking_url_template") or a.get("url_custom_parameters"):
            anuncios.append({
                "ad_id": a.get("id"),
                "campanha": r.get("campaign", {}).get("name"),
                "final_urls": list(urls),
                "tracking_url_template": a.get("tracking_url_template"),
                "custom_params": _params_to_dict(a.get("url_custom_parameters")),
            })

    print_json({"campanhas": campanhas, "anuncios_com_utm_propria": anuncios})


# ---------------------------------------------------------------------------
# campaign-params
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_campaign_params(args):
    """Altera url_custom_parameters da campanha preservando as chaves nao citadas."""
    cid = resolve_customer_id(args.customer_id)
    client = init_client()

    novos = {}
    for item in args.set:
        if "=" not in item:
            print_error(f"--set espera chave=valor, recebi: {item}")
            sys.exit(1)
        k, v = item.split("=", 1)
        novos[k.strip()] = v.strip()

    q = f"""SELECT campaign.id, campaign.name, campaign.url_custom_parameters
            FROM campaign WHERE campaign.id = {args.campaign_id}"""
    rows = run_query(cid, q)
    if not rows:
        print_error(f"campanha {args.campaign_id} nao encontrada na conta {cid}")
        sys.exit(1)

    c = rows[0].get("campaign", {})
    atuais = _params_to_dict(c.get("url_custom_parameters"))
    final = dict(atuais)
    final.update(novos)

    print(f"campanha [{c.get('id')}] {c.get('name')}")
    for k in sorted(set(list(atuais) + list(final))):
        antes, depois = atuais.get(k), final.get(k)
        marca = "   " if antes == depois else ">> "
        print(f"  {marca}{k}: {antes!r} -> {depois!r}")

    if not args.apply:
        print("\nDRY-RUN. Nada foi escrito. Repita com --apply para aplicar.")
        return

    from google.api_core import protobuf_helpers

    service = client.get_service("CampaignService")
    op = client.get_type("CampaignOperation")
    campaign = op.update
    campaign.resource_name = service.campaign_path(cid, args.campaign_id)
    for k, v in final.items():
        p = client.get_type("CustomParameter")
        p.key = k
        p.value = v
        campaign.url_custom_parameters.append(p)
    client.copy_from(op.update_mask, protobuf_helpers.field_mask(None, campaign._pb))

    resp = service.mutate_campaigns(customer_id=cid, operations=[op])
    print(f"\nOK: {resp.results[0].resource_name}")


# ---------------------------------------------------------------------------
# ad-final-url
# ---------------------------------------------------------------------------

@handle_google_error_decorator
def cmd_ad_final_url(args):
    """Troca a(s) final_urls de um anuncio."""
    cid = resolve_customer_id(args.customer_id)
    client = init_client()

    q = f"""SELECT campaign.name, ad_group.id, ad_group_ad.ad.id, ad_group_ad.ad.final_urls
            FROM ad_group_ad WHERE ad_group_ad.ad.id = {args.ad_id}"""
    rows = run_query(cid, q)
    if not rows:
        print_error(f"anuncio {args.ad_id} nao encontrado na conta {cid}")
        sys.exit(1)

    a = rows[0].get("ad_group_ad", {}).get("ad", {})
    antes = list(a.get("final_urls") or [])
    print(f"anuncio [{a.get('id')}] em {rows[0].get('campaign', {}).get('name')}")
    print(f"  antes : {antes}")
    print(f"  depois: {args.url}")

    if not args.apply:
        print("\nDRY-RUN. Nada foi escrito. Repita com --apply para aplicar.")
        return

    from google.api_core import protobuf_helpers

    service = client.get_service("AdService")
    op = client.get_type("AdOperation")
    ad = op.update
    ad.resource_name = service.ad_path(cid, args.ad_id)
    ad.final_urls.append(args.url)
    client.copy_from(op.update_mask, protobuf_helpers.field_mask(None, ad._pb))

    resp = service.mutate_ads(customer_id=cid, operations=[op])
    print(f"\nOK: {resp.results[0].resource_name}")


def main():
    parser = argparse.ArgumentParser(description="Google Ads - leitura e edicao do rastreamento (UTM)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("show", help="Mostra template, parametros por campanha e UTM em URL de anuncio")
    add_customer_arg(p)
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("campaign-params", help="Altera url_custom_parameters da campanha")
    add_customer_arg(p)
    p.add_argument("--campaign-id", required=True)
    p.add_argument("--set", nargs="+", required=True, metavar="CHAVE=VALOR",
                   help="Chaves nao citadas sao preservadas")
    p.add_argument("--apply", action="store_true", help="Escreve de verdade (sem isso e dry-run)")
    p.set_defaults(func=cmd_campaign_params)

    p = sub.add_parser("ad-final-url", help="Troca a final_url de um anuncio")
    add_customer_arg(p)
    p.add_argument("--ad-id", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--apply", action="store_true", help="Escreve de verdade (sem isso e dry-run)")
    p.set_defaults(func=cmd_ad_final_url)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
