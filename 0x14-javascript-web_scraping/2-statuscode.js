#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request.get(url, (err, data) => {
  if (err) console.error(err);
  else console.log(JSON.parse(data.body).title);
});
