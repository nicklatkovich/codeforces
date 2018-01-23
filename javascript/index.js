
const fs = require('fs');
const input = fs.readFileSync(__dirname + '/input.txt').toString().split('\n');
let readline = () => {
	return input.shift();
}
let print = (value) => {
	console.log(value);
}

module.exports = { readline, print };
