#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((idx, value) => idx * value);
console.log(list);
console.log(newList);
