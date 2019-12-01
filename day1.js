const fs = require('fs');
const input = fs.readFileSync('day1input.txt', {encoding: 'utf8'}).split("\n");

const fuelRequired = modules => {
    return modules.map(m => Math.floor(+m / 3) - 2).reduce((acc, w) => acc + w);
};

console.log(fuelRequired(input));