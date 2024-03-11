#!/usr/bin/node
const { argv } = require('node:process');
console.log((argv[2] !== undefined) ? argv[2] : 'No argument');
