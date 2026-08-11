#!/usr/bin/env python3
"""
Auto Pause — pausa anúncios que gastaram acima do limite sem gerar lead.

Rode SEMPRE com --dry-run antes de valer. Ele pausa anúncios de verdade.

Uso:
  python auto_pause.py --campaign <ID> --dry-run              (só mostra)
  python auto_pause.py --campaign <ID> --threshold 500        (pausa de verdade)

A campanha é obrigatória de propósito: não existe padrão embutido, para não
correr o risco de agir na campanha errada.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Carrega .env
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ[k.strip()] = v.strip().strip('"')

sys.path.insert(0, str(Path(__file__).parent / 'lib'))

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adsinsights import AdsInsights

# Sem campanha padrão: o ID vem sempre por --campaign.

def get_cpl(costs):
    for c in costs:
        if c.get('action_type') in [
            'offsite_submit_application_add_meta_leads',
            'offsite_contact_website_add_meta_leads'
        ]:
            return float(c.get('7d_click', c.get('value', 0)))
    return 0

def check_and_pause(campaign_id, config, dry_run=True):
    api = FacebookAdsApi.get_default_api()
    campaign = Campaign(campaign_id)

    # Busca todos os ads ativos da campanha
    ads = campaign.get_ads(
        fields=['id', 'name', 'status', 'effective_status']
    )
    active_ads = [a for a in ads if a.get('effective_status') == 'ACTIVE']

    if not active_ads:
        print(f"  Sem anúncios ativos.")
        return []

    paused = []
    threshold = config['threshold_brl']

    print(f"\n{'AD':<45} {'GASTO 7d':>10} {'LEADS':>6} {'DECISÃO'}")
    print("-" * 75)

    for ad in active_ads:
        # Busca insights últimos 7 dias
        insights = ad.get_insights(
            fields=[
                AdsInsights.Field.spend,
                AdsInsights.Field.actions,
                AdsInsights.Field.cost_per_action_type,
            ],
            params={
                'date_preset': 'last_7d',
                'action_attribution_windows': ['7d_click'],
            }
        )

        if not insights:
            print(f"  {ad['name']:<45} {'sem dados':>10}")
            continue

        d = insights[0]
        spend = float(d.get('spend', 0))
        costs = d.get('cost_per_action_type', [])
        cpl = get_cpl(costs)
        leads = round(spend / cpl) if cpl > 0 else 0

        name = ad['name'][:44]
        spend_str = f"R${spend:,.0f}"

        if spend >= threshold and leads == 0:
            decision = "⏸  PAUSAR" if not dry_run else "⏸  PAUSARIA"
            print(f"  {name:<45} {spend_str:>10} {leads:>6}   {decision}")
            if not dry_run:
                try:
                    ad_obj = Ad(ad['id'])
                    ad_obj.api_update(params={'status': 'PAUSED'})
                    paused.append({'id': ad['id'], 'name': ad['name'], 'spend': spend})
                    time.sleep(1)
                except Exception as e:
                    print(f"    Erro ao pausar {ad['id']}: {e}")
        else:
            cpl_str = f"R${cpl:,.0f}" if cpl > 0 else "-"
            status = "✓ OK" if leads > 0 else "— aguardando"
            print(f"  {name:<45} {spend_str:>10} {leads:>6}   {status} (CPL {cpl_str})")

        time.sleep(0.3)

    return paused

def main():
    parser = argparse.ArgumentParser(description='Auto Pause — pausa anúncios sem resultado')
    parser.add_argument('--dry-run', action='store_true', help='Só mostra, não executa pausas')
    parser.add_argument('--campaign', required=True, help='ID da campanha (obrigatório)')
    parser.add_argument('--threshold', type=int, default=500, help='Gasto mínimo em R$ para pausar (default: 500)')
    args = parser.parse_args()

    token = os.environ.get('META_ADS_TOKEN', '')
    if not token:
        print("ERRO: META_ADS_TOKEN não encontrado no .env")
        sys.exit(1)

    FacebookAdsApi.init(access_token=token)

    mode = "DRY RUN (sem pausas reais)" if args.dry_run else "EXECUÇÃO REAL"
    print(f"\n{'='*60}")
    print(f"Auto Pause — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Modo: {mode}")
    print(f"Regra: gasto ≥ R${args.threshold} em 7 dias sem lead → PAUSAR")
    print(f"{'='*60}")

    campaigns = {
        args.campaign: {
            'name': f'Campanha {args.campaign}',
            'threshold_brl': args.threshold,
            'window_days': 7,
        }
    }

    total_paused = []
    for cid, config in campaigns.items():
        config['threshold_brl'] = args.threshold
        print(f"\n▶ {config['name']} ({cid})")
        paused = check_and_pause(cid, config, dry_run=args.dry_run)
        total_paused.extend(paused)

    print(f"\n{'='*60}")
    if args.dry_run:
        print(f"DRY RUN concluído. Para executar de verdade, rode sem --dry-run.")
    else:
        print(f"Total pausados: {len(total_paused)}")
        for p in total_paused:
            print(f"  ⏸  {p['name']} (R${p['spend']:,.0f} gastos)")

if __name__ == '__main__':
    main()
