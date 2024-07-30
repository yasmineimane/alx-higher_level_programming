#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
  } else {
    try {
      const filmData = JSON.parse(body).results;
      const filmWithWedge = filmData.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );
      console.log(filmWithWedge.length);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError.message);
    }
  }
});
