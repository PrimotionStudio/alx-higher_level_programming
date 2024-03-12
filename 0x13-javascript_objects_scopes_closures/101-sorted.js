#!/usr/bin/node
const dict = require('./101-data.js');
let new = {};
for (let key in dict) {
  let n_key = dict[key];
  for (let key in dict) {
    if (dict[key] == n_key) {
      new.n_key = key;
    }
  }
}
