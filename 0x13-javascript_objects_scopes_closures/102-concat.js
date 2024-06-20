#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const firstContent = fs.readFileSync(args[0], 'utf8');
const secondContent = fs.readFileSync(args[1], 'utf8');
const res = `${firstContent}\n${secondContent}\n`;
fs.writeFileSync(args[2], res, 'utf8');
