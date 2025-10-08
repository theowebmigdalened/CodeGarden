#!/usr/bin/env bash
set -euo pipefail
JITTER_MAX=600
sleep $((RANDOM % JITTER_MAX))
# 1) подгружаем .env
set -a
[ -f "$HOME/.env" ] && . "$HOME/.env"
set +a

# 2) диагностика окружения
{
  echo "[$(date -Is)] DIAG: whoami=$(id -un) HOME=$HOME"
  echo "[$(date -Is)] DIAG: TOKEN_LEN=${#TELEGRAM_TOKEN} CHAT_ID=${TELEGRAM_CHAT_ID:-<empty>}"
  echo "[$(date -Is)] DIAG: PATH=$PATH"
} >> /root/codegarden/cron.log

# 3) запуск планировщика
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd /root/codegarden
/usr/bin/python3 -m auto_updater.scheduler >> /root/codegarden/cron.log 2>&1
