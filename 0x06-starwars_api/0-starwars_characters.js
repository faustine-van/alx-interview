#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const process = require('process');
const args = process.argv;
const id = args[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function fetchCharacters (url) {
  try {
    const response = await new Promise((resolve, reject) => {
      request(url, (error, res, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });
    const film = JSON.parse(response);
    const urlCharacters = film.characters;

    for (const urlCharacter of urlCharacters) {
      const characterResponse = await new Promise((resolve, reject) => {
        request(urlCharacter, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(body);
          }
        });
      });
      const character = JSON.parse(characterResponse);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching characters:', error);
  }
}
fetchCharacters(url);
