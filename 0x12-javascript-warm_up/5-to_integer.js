#!/usr/bin/node
const { argv } = require('node:process');
console.log(isNaN(parseInt(argv[2])) ? 'Not a number' : 'My number: ' + argv[2]);
