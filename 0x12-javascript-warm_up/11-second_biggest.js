#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else if (argv.length === 4) {
  if (parseInt(argv[2]) > (parseInt(argv[3])))
    console.log(argv[3]);
  else
    console.log(argv[2]);
} else {
  let i = 2;
  let max = parseInt(argv[i]);
  while (true) {
    if (isNaN(parseInt(argv[i]))) {
      break;
    }
    if (parseInt(argv[i]) > max) {
      max = parseInt(argv[i]);
    }
    i++;
  }
  let j = 2;
  let nextMax = parseInt(argv[j]);
  while (j < i) {
    if (parseInt(argv[j]) > nextMax && parseInt(argv[j]) !== max) {
      nextMax = parseInt(argv[j]);
    }
    j++;
  }
  console.log(nextMax);
}
