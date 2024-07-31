#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Failed to retrieve film data. Status code: ${response.statusCode}`);
    return;
  }

  const content = JSON.parse(body);
  const characters = content.characters;

  characters.forEach((character) => {
    request.get(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log(`Failed to retrieve character data. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

