#!/usr/bin/env bash
cd /app || exit
rm -rf node_modules
npm cache clean --force
npm install
npm run start
tail -f /dev/null