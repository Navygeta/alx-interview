#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

const fetchCharacterNames = (characters) => {
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
};

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  fetchCharacterNames(film.characters);
});
