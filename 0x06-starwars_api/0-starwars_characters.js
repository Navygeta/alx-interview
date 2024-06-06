#!/usr/bin/node

const request = require('request'); // Import the request module
const filmId = process.argv[2]; // Get the Movie ID from the command line arguments
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`; // Construct the URL for the film

// Request the film data from the Star Wars API
request(url, (err, response, body) => {
  if (err) {
    console.error(err); // Log any error that occurs
    return;
  }
  const film = JSON.parse(body); // Parse the response body to get the film data
  const characters = film.characters; // Extract the list of character URLs

  /**
   * Function to request and print a character's name
   * @param {string} characterUrl - The URL of the character
   * @param {function} callback - The callback function to execute after printing the name
   */
  const printCharacterName = (characterUrl, callback) => {
    request(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err); // Log any error that occurs
        return callback(err); // Return error to callback
      }
      const character = JSON.parse(body); // Parse the response body to get the character data
      console.log(character.name); // Print the character's name
      callback(); // Invoke the callback to proceed to the next character
    });
  };

  /**
   * Function to recursively print all character names
   * @param {number} index - The current index in the characters array
   */
  const printAllCharacters = (index) => {
    if (index >= characters.length) {
      return; // Stop recursion if all characters have been printed
    }
    printCharacterName(characters[index], () => {
      printAllCharacters(index + 1); // Move to the next character
    });
  };

  printAllCharacters(0); // Start printing characters from the first one
});
