#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];
request.get(url, (err, data) => {
  if (err) console.error(err);
  else {
    const html = JSON.parse(data.body);
    fs.writeFile(file, html, {encoding: 'utf-8'}, (err) => {
    	console.error(err);
    });
  }
});
