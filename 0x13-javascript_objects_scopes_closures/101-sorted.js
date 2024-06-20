#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const val in dict) {
  if (!newDict[dict[val]]) {
    newDict[dict[val]] = [];
  }
  newDict[dict[val]].push(val);
}
console.log(newDict);
