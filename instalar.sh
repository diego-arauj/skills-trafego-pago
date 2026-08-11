#!/usr/bin/env bash
# Instala as skills de tráfego pago no Claude Code.
# Rode de dentro da pasta do repositório:  bash instalar.sh
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/.claude/skills"

echo "Repositório: $REPO"
echo "Instalando em: $DEST"
echo

mkdir -p "$DEST"

for item in meta-ads google-ads kb; do
  alvo="$DEST/$item"
  if [ -e "$alvo" ] && [ ! -L "$alvo" ]; then
    echo "  ATENÇÃO: já existe $alvo e não é um link. Não vou mexer."
    echo "           Renomeie ou apague antes de rodar de novo."
    continue
  fi
  ln -sfn "$REPO/$item" "$alvo"
  echo "  ok  $item"
done

echo
echo "As skills leem a base de conhecimento em ../kb, por isso a pasta kb também"
echo "é linkada aqui (ela não é uma skill; o Claude Code ignora pasta sem SKILL.md)."
echo

# Dependências
echo "Instalando os SDKs..."
pip3 install --quiet facebook-business google-ads google-auth-oauthlib protobuf || {
  echo "  Falhou. Rode na mão: pip3 install facebook-business google-ads google-auth-oauthlib protobuf"
}

# .env de exemplo
for skill in meta-ads google-ads; do
  if [ ! -f "$REPO/$skill/.env" ]; then
    cp "$REPO/$skill/.env.example" "$REPO/$skill/.env"
    echo "  criado $skill/.env (vazio, para você preencher)"
  fi
done

cat <<'FIM'

Pronto. Agora abra o Claude Code e peça:

    "roda o setup da skill de meta ads"

Depois:

    "me ajuda a configurar a skill de google ads"

Ele conduz o resto: cria o app, gera os tokens e resolve o acesso às contas.
Comece pela Meta: o setup dela leva 20 minutos, e o do Google tem uma etapa de
aprovação que pode levar um dia.
FIM
