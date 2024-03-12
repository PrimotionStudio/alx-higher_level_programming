#!/usr/bin/node
const dict = require('./101-data.js');
let newDict = {};
const keys = Object.keys(dict.dict);
const vals = new Set(Object.values(dict.dict));
vals.forEach(val => {
    let numArray = [];
  keys.forEach(key => {
    if (dict.dict[key] === val) {
      numArray.push(key);
    }
  });
  newDict[val] = numArray;
});

console.log(newDict);