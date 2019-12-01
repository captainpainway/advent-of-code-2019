const fs = require('fs');
const input = fs.readFileSync('day1input.txt', {encoding: 'utf8'}).split("\n");

const calcFuel = amt => {
    return Math.floor(amt / 3) - 2;
};

const fuelRequired = modules => {
    return modules.map(m => calcFuel(+m)).reduce((acc, w) => acc + w);
};

const totalFuelRequired = modules => {
    return modules.map(m => {
        let total = 0;
        let current = calcFuel(+m);
        while (current > 0) {
            total += current;
            current = calcFuel(current);
        }
        return total;
    }).reduce((acc, w) => acc + w);
};

console.log("Part 1: " + fuelRequired(input));

console.log("Part 2: " + totalFuelRequired(input));