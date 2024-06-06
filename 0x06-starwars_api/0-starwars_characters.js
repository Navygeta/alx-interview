#!/usr/bin/node
/**
 * Request wrapper for async/await
 * @param {String} url - URL to request
 * @returns {Promise} - Resolves with parsed JSON response, rejects on error
 */
function makeRequest(url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Fetches and prints Star Wars character names for a given movie ID
 */
async function main() {
  const args = process.argv;
  if (args.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  const movie = await makeRequest(movieUrl);
  if (!movie.characters) return;

  for (const characterUrl of movie.characters) {
    const character = await makeRequest(characterUrl);
    console.log(character.name);
  }
}

main();
