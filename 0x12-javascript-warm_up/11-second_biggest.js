#!/usr/bin/node
const arr = process.argv.slice();
if (isNaN(parseInt(arr[2]))) {
  console.log(0);
} else if (arr.length - 2 === 1) {
  console.log(0);
} else {
  let maxVal = parseInt(arr[2]);
  let secondMaxVal = parseInt(arr[3]);
  for (let i = 3; i < arr.length; i++) {
    const num = parseInt(arr[i]);
    if (num > maxVal) {
      secondMaxVal = maxVal;
      maxVal = num;
    } else if (num > secondMaxVal && num !== maxVal) {
      secondMaxVal = num;
    }
  }
  console.log(secondMaxVal);
}
