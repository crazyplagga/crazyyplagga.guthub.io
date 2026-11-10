#!/bin/bash
cd "$(dirname "$0")"
read -s -p "Токен бота от BotFather: " BOT_TOKEN
echo
read -p "Адрес GitHub Pages (https://ВАШ-ЛОГИН.github.io/ИМЯ-РЕПОЗИТОРИЯ/): " WEBAPP_URL
case "$WEBAPP_URL" in
  https://*) ;;
  *) echo "Нужен публичный HTTPS-адрес GitHub Pages."; read -p "Нажми Enter для выхода"; exit 1 ;;
esac
export BOT_TOKEN WEBAPP_URL
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
pip install -q -r requirements.txt
python bot.py
