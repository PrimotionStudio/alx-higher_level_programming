#!/usr/bin/node
const request = require('request');

const id = 18;
const url = `https://swapi-api.alx-tools.com/api/people/${id}`;
request.get(url, (err, data) => {
  if (err) console.error(err);
  else console.log(JSON.parse(data.body).films.length);
});
