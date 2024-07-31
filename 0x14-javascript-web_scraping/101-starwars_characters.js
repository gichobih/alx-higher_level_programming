#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve film data. Status code:', response.statusCode);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  for (const characterUrl of characterUrls) {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Failed to retrieve character data. Status code:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});

