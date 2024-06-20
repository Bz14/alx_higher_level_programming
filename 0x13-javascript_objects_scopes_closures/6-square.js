#!/usr/bin/node
const Sq = require('./5-square.js');
class Square extends Sq {
  charPrint (c) {
    let chr = c;
    if (c === undefined) {
      chr = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(chr.repeat(this.height));
    }
  }
}
module.exports = Square;
