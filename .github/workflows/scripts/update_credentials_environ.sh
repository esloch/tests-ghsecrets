#!/usr/bin/env bash


# CLIENT_SECRETS = '*'
sed -i -e "s|^CLIENTE_SECRETS=.*$|CLIENTE_SECRETS=$CLIENTE_SECRETS|g" .env
# CLIENT_ID='*'
sed -i -e "s|^CLIENTE_ID=.*$|CLIENTE_ID=$CLIENTE_ID|g" .env
# PROJECT_ID='*'
sed -i -e "s|^PROJETO_ID=.*$|PROJETO_ID=$PROJETO_ID|g" .env
# REFRESH_TOKEN='*'
sed -i -e "s|^REFRESCA_TOKEN=.*$|REFRESCA_TOKEN=$REFRESCA_TOKEN|g" .env
# ACCESS_TOKEN
sed -i -e "s|^ACESSO_TOKEN=.*$|ACESSO_TOKEN=$ACESSO_TOKEN|g" .env

echo "Environment variables were exported!"
