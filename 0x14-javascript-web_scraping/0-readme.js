#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, data) {
  error ? console.log(error) : console.log(data);
});
