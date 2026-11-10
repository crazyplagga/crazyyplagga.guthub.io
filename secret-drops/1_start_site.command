#!/bin/bash
cd "$(dirname "$0")"
if ! command -v cloudflared >/dev/null 2>&1; then
  echo "Не найден cloudflared. Установи его командой:  brew install cloudflared"
  echo "(если нет brew - см. README.txt)"
  read -p "Нажми Enter для выхода"; exit 1
fi
python3 -m http.server 8000 --directory webapp >/dev/null 2>&1 &
SERVER_PID=$!
trap 'kill "$SERVER_PID" 2>/dev/null || true' EXIT
echo "Ищи в тексте ниже адрес https://....trycloudflare.com и скопируй его."
echo "Это окно не закрывай. Потом запусти 2_start_bot.command"
cloudflared tunnel --protocol http2 --url http://localhost:8000
