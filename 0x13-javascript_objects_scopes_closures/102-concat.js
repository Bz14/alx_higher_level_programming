#!/usr/bin/node
const fs = require('fs');
const arr = process.argv;
const data1 = fs.readFileSync(arr[2], 'utf8');
const data2 = fs.readFileSync(arr[3], 'utf8');
const concatenatedData = data1 + '\n' + data2 + '\n';
fs.writeFileSync(arr[4], concatenatedData);
