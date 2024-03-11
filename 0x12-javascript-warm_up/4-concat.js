#!/usr/bin/node
const { argv } = require("node:process");
console.log((argv[2] === undefined) ? "undefined" : argv[2], "is", (argv[3] === undefined) ? "undefined" : argv[3]);
