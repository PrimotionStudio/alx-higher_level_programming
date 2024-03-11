#!/usr/bin/node
const { argv } = require('node:process');
let i = 0;
let row = '';
const j = parseInt(argv[2]);
if (!isNaN(j)) {
  while (i < j) {
    let k = 0;
    while (k < j) {
      row = row + 'X';
      k++;
    }
    console.log(row);
    row = '';
    i++;
  }
} else {
  console.log('Missing size');
}
