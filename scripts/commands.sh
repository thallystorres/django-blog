#!/bin/sh

# O shell irá encessar a execução se der algum erro :P
set -e

wait_psql.sh
collectstatic.sh
makemigrations.sh
migrate.sh
runserver.sh