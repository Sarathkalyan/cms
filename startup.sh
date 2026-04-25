#!/bin/bash

echo "--- Installing ODBC Driver 17 ---"
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg || true
curl -fsSL https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list || true
apt-get update -qq || true
ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev 2>/dev/null || true

echo "--- Starting gunicorn ---"
gunicorn --bind=0.0.0.0:8000 --timeout=600 --workers=2 application:app
