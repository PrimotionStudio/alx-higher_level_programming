#!/usr/bin/node
const { argv } = require('node:process');
const i = parseInt(argv[2]);
if (isNaN(i)) {
  console.log(1);
} else {
  console.log(factorial(i));
}
function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
