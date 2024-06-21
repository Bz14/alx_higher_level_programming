#!/usr/bin/node
const args = process.argv.slice(2);
if (isNaN(args[0]) || args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg));
  const firstMax = Math.max(...numbers);
  let secondMax = 0;
  for (const i in numbers) {
    if (numbers[i] !== firstMax) {
      secondMax = Math.max(secondMax, numbers[i]);
    }
  }
  console.log(secondMax);
}
