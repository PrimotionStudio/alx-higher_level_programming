#!/usr/bin/node
const { argv } = require('node:process');
let i = 0;
const j = parseInt(argv[2]);
if (!isNaN(j)) {
  while (i < j) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
