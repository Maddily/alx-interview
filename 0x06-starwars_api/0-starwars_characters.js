#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);
const filmId = process.argv[2];

if (!filmId) {
  console.log('Please pass the id of a film');
} else {
  const filmsUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

  // Display all characters of a Star Wars film.
  request(filmsUrl, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characterUrls = JSON.parse(body).characters;

    for (const characterUrl of characterUrls) {
      try {
        const characterResponse = await requestPromise(characterUrl);
        const characterName = JSON.parse(characterResponse.body).name;
        console.log(characterName);
      } catch (error) {
        console.error(error);
      }
    }
  });
}
