#!/usr/bin/node

const request = require('request');
const results = {};

request(process.argv[2], function (error, response, body) {
  for (const entry of JSON.parse(body)) {
    if (error) console.log(error);
    if (results[entry.userId] === undefined) results[entry.userId] = 0;
    if (entry.completed === true) results[entry.userId]++;
  }
  console.log(results);
});
