#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
fs.readFile(args[0], 'utf8', (err, firstContent) => {
  if (err) {
    console.log('Error');
    return;
  }
  fs.readFile(args[1], 'utf8', (err, secondContent) => {
    if (err) {
      console.log('Error');
      return;
    }
    const res = firstContent + '\n' + secondContent + '\n';
    fs.writeFile(args[2], res, 'utf8', (err) => {
      if (err) {
        console.log('Error');
      }
    });
  });
});
