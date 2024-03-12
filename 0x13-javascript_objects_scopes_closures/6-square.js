#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.height) {
        let j = 0;
        let row = '';
        while (j < this.width) {
          row = row + 'C';
          j++;
        }
        console.log(row);
        i++;
      }
    }
  }
};
