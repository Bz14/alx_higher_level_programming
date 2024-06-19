#!/usr/bin/node
function factorial (num) {
  if (num === 0 || num === 1) {
    return num;
  }
  return num * factorial(num - 1);
}
const args = process.argv.slice(2);
if (isNaN(args[0])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(args[0])));
}
