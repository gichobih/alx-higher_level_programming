#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
  } else {
    if (response.statusCode === 200) {
      const content = JSON.parse(body);
      const characters = content.characters;
      for (const character of characters) {
        request.get(character, (error, response, body) => {
          if (error) {
            console.error('Error fetching character data:', error);
          } else {
            if (response.statusCode === 200) {
              const names = JSON.parse(body);
              console.log(names.name);
            } else {
              console.error(`Failed to retrieve character data. Status code: ${response.statusCode}`);
            }
          }
        });
      }
    } else {
      console.error(`Failed to retrieve film data. Status code: ${response.statusCode}`);
    }
  }
});

