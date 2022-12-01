#!/usr/bin/node

const dict = require('./101-data').dict;
const occur = {};

for (const key in dict) {
  if (!occur[dict[key]]) occur[dict[key]] = [];
  occur[dict[key]].push(key);
}

console.log(occur);
