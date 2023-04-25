#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const jsObj = (JSON.parse(body));
    const chars = jsObj.characters;
    for (const x of chars) {
      req(x, function (error, response, body) {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          console.log((JSON.parse(body)).name);
        } else {
          console.log('Character not found. Error code: ' + response.statusCode);
        }
      });
    }
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
