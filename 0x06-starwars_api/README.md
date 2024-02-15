# 0x06. Star Wars API

## Run project
### Installation
Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
Install semi-standard
[Documentation](https://github.com/standard/semistandard)

`$ sudo npm install semistandard --global`

Install request module and use it
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

#### using request locally

Create a New Node.js Project (if you haven't already):
```
$ mkdir my-project
$ cd my-project
$ npm init -y
```
Install the request Module Locally:

`npm install request`

Create a JavaScript File:

Write Code to Use the request Module:

`javascript`
```
const request = require('request');

// Making a GET request
request('https://jsonplaceholder.typicode.com/posts/1', function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body); // Print the response body.
  }
});
```
Run the Script:
 ```
 node file.js` # or 
 $ chmod a+x file.js
 ./file.js
 ```
## Task
```s
Write a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
```

### Reference
- [Making HTTP Requests in Node.js](https://www.geeksforgeeks.org/node-js-request-module/)
[Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
[Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
[Node.js Process & Command Line Arguments](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/)
[JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
