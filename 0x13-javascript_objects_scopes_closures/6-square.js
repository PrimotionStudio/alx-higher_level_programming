#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
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
