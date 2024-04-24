#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request.get(url, (err, data, html) => {
  if (err) console.error(err);
  else {
    fs.writeFile(file, html, { encoding: 'utf-8' }, () => {});
  }
});
