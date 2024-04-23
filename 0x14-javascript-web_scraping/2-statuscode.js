#!/usr/bin/node
const request = require("request");

const url = process.argv[2];
request.get(url, (err, data) => {
	if (err) console.error(err);
	else console.log(`code: ${data}`);
});