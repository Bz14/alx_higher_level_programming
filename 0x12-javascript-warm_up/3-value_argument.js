#!/usr/bin/node
const args = process.argv.slice();
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
