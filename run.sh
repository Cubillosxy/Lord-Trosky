#!/bin/bash

cd ./blog
echo "** Instalando dependencias ** "
npm install
echo "** compilando stats.prod.json **"
npm run build:prod
echo "Iniciando node server ..."
node server.js
echo "run server on localhost:3000 "