#!/usr/bin/node
const { argv } = require('node:process');
const i = parseInt(argv[2]);
const j = parseInt(argv[3]);
if (isNaN(i) || isNaN(j)) {
  console.log('NaN');
} else {
  console.log(i + j);
}
