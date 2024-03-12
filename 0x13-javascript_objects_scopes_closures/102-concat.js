#!/usr/bin/node
const fs = require('fs');
const [, , fileA, fileB, fileC] = process.argv;
fs.readFile(fileA, 'utf8', (err, a) => {
  if (err) {
    return;
  }
  fs.readFile(fileB, 'utf8', (err, b) => {
    if (err) {
      return;
    }
    const concatenatedData = a + b;
    fs.writeFile(fileC, concatenatedData, 'utf8', () => {});
  });
});
