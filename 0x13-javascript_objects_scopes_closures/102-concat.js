#!/usr/bin/node
const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;
fs.readFile(fileA, 'utf8', (err, a) => {
  fs.readFile(fileB, 'utf8', (err, b) => {
    const concatenatedData = a + b;
    fs.writeFile(fileC, concatenatedData, 'utf8', () => {});
  });
});

