#!/usr/bin/node

const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);
fs.writeFile(process.argv[4], fileA + fileB);

// Ref: https://stackoverflow.com/questions/30694472/nodejs-how-to-copy-multiple-files-into-one
// Ref: https://stackoverflow.com/questions/10058814/get-data-from-fs-readfile
