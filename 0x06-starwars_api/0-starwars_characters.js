#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  
  const printCharacterName = (characterUrl, callback) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return callback(err);
      }
      const character = JSON.parse(body);
      console.log(character.name);
      callback();
    });
  };

  const printAllCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }
    printCharacterName(characters[index], () => {
      printAllCharacters(index + 1);
    });
  };

  printAllCharacters(0);
});
