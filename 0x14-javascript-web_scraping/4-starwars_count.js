#!/usr/bin/node
const request = require('request');

const id = 'https://swapi-api.alx-tools.com/api/people/18/';
const url = 
process.argv[2];
request.get(url, (err, data) => {
  if (err) console.error(err);
  else {
    const films = JSON.parse(data.body).results;
    let count = 0;
    films.forEach((film) => {
      if (film.characters.includes(id)) count++;
    });
    console.log(count);
  }
});
