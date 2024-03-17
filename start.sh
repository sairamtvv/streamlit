#!/bin/bash

SERVER_PORT=${SERVER_PORT:-8011}

streamlit run ./app.py \
  --server.port ${SERVER_PORT} \
  --server.enableCORS false \
  --server.enableXsrfProtection false
