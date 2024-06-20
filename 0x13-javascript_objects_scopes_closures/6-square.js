#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
