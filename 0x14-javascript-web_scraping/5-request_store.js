#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (wErr) => {
      if (wErr) {
        console.log(wErr);
      }
    });
  }
});
