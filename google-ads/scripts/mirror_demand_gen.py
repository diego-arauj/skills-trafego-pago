#!/usr/bin/env python3
"""Espelha os anuncios de uma campanha Demand Gen num ad group de destino.

Existe porque Demand Gen com audience_setting.use_audience_grouped=True recusa reaproveitar
o mesmo anuncio em varios ad groups (AD_SHARING_NOT_ALLOWED): cada ad group precisa das suas
proprias copias. Este script copia o criativo inteiro com CopyFrom, preservando tudo.

Cria SEMPRE como PAUSED. Ativar e decisao sua, na interface ou pelo update.py.
E idempotente: anuncio que ja existe no destino (mesmo nome) e pulado.

Uso:
  mirror_demand_gen.py --customer-id 1234567890 \\
                       --source-campaign-id 23666639998 \\
                       --target-ad-group-id 987654321 \\
                       [--exclude "NOME A|NOME B"] [--dry-run]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import init_client, run_query  # noqa: E402

FIELDS = """ad_group_ad.ad.name, ad_group_ad.ad.final_urls,
ad_group_ad.ad.demand_gen_video_responsive_ad.headlines,
ad_group_ad.ad.demand_gen_video_responsive_ad.long_headlines,
ad_group_ad.ad.demand_gen_video_responsive_ad.descriptions,
ad_group_ad.ad.demand_gen_video_responsive_ad.videos,
ad_group_ad.ad.demand_gen_video_responsive_ad.business_name,
ad_group_ad.ad.demand_gen_video_responsive_ad.call_to_actions,
ad_group_ad.ad.demand_gen_video_responsive_ad.logo_images,
ad_group_ad.ad.demand_gen_video_responsive_ad.breadcrumb1,
ad_group_ad.ad.demand_gen_video_responsive_ad.breadcrumb2"""


def main():
    ap = argparse.ArgumentParser(description="Espelha anuncios de Demand Gen num ad group destino")
    ap.add_argument("--customer-id", required=True, help="Conta (sem hifens)")
    ap.add_argument("--source-campaign-id", required=True, help="Campanha de origem dos criativos")
    ap.add_argument("--target-ad-group-id", required=True, help="Ad group que vai receber as copias")
    ap.add_argument("--exclude", default="", help="Nomes de anuncio a pular, separados por |")
    ap.add_argument("--dry-run", action="store_true", help="So mostra o que copiaria")
    args = ap.parse_args()

    cid = args.customer_id
    target = args.target_ad_group_id
    exclude = {n.strip() for n in args.exclude.split("|") if n.strip()}

    client = init_client()
    ga = client.get_service("GoogleAdsService")
    svc = client.get_service("AdGroupAdService")
    ag_path = ga.ad_group_path(cid, target)

    # origem: um ad_id por nome, so os ENABLED da campanha de origem
    src = {}
    q = (f"SELECT ad_group_ad.ad.id, ad_group_ad.ad.name FROM ad_group_ad "
         f"WHERE campaign.id={args.source_campaign_id} AND ad_group_ad.status='ENABLED'")
    for r in run_query(cid, q):
        nm = r["ad_group_ad"]["ad"].get("name")
        src.setdefault(nm, r["ad_group_ad"]["ad"]["id"])
    wanted = {n for n in src if n and n not in exclude}

    # o que ja existe no destino, em qualquer status
    present = set()
    q = (f"SELECT ad_group_ad.ad.name, ad_group_ad.status FROM ad_group_ad "
         f"WHERE ad_group.id={target}")
    for r in run_query(cid, q):
        present.add(r["ad_group_ad"]["ad"].get("name"))

    missing = sorted(n for n in wanted if n not in present)
    print(f"origem={len(wanted)} | ja no destino={len(wanted) - len(missing)} | a copiar={len(missing)}")
    if not missing:
        return
    for n in missing:
        print(f"  - {n}")
    if args.dry_run:
        print("\n(dry-run: nada foi criado)")
        return

    ids = ",".join(src[n] for n in missing)
    ops = []
    for row in ga.search(customer_id=cid,
                         query=f"SELECT {FIELDS} FROM ad_group_ad WHERE ad_group_ad.ad.id IN ({ids})"):
        s = row.ad_group_ad.ad
        op = client.get_type("AdGroupAdOperation")
        c = op.create
        c.ad_group = ag_path
        c.status = client.enums.AdGroupAdStatusEnum.PAUSED
        c.ad.name = s.name
        for u in s.final_urls:
            c.ad.final_urls.append(u)
        c.ad.demand_gen_video_responsive_ad._pb.CopyFrom(s.demand_gen_video_responsive_ad._pb)
        ops.append(op)

    resp = svc.mutate_ad_group_ads(customer_id=cid, operations=ops)
    print(f"\ncriados PAUSED: {len(resp.results)}")
    print("Revise na interface e ative depois (update.py ad --status ENABLED).")


if __name__ == "__main__":
    main()
