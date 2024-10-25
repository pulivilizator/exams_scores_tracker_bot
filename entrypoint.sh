#!/bin/sh

alembic upgrade head

if [ $? -eq 0 ]; then
  exec python3 -m bot
else
  echo "Migrations failed. Exiting."
  exit 1
fi