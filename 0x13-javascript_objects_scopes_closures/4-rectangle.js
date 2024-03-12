#!/usr/bin/node
module.exports = class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    let i = 0
    while (i < this.height) {
      let j = 0;
      let row = '';
      while (j < this.width) {
        row = row + 'X';
        j++;
      }
      console.log(row);
      i++;
    }
  }
  rotate() {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
  double() {
    this.width *= 2;
    this.height *= 2;
  }
};
