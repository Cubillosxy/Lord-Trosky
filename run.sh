#!/bin/bash

cd ./blog
echo "** Installing packages ** "
npm install
echo "** Updating packages**"
npm update
echo "** building stats.prod.json **"
npm run build:prod
echo "start node server ..."
node server.js
echo "run server on localhost:3000 "