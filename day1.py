import math
from functools import reduce

input = open('day1input.txt').read().splitlines()

def calcFuel(amt):
    return math.floor(int(amt) / 3) - 2

def addFuel(f1, f2):
    return f1 + f2;

def fuelRequired(modules):
    return reduce(addFuel, map(calcFuel, modules))

def additionalFuelNeeded(fuel):
    total = 0
    current = calcFuel(int(fuel))
    while(current > 0):
        total += current
        current = calcFuel(current)
    return total

def totalFuelRequired(modules):
    return reduce(addFuel, map(additionalFuelNeeded, modules))

print("Part 1: " + str(fuelRequired(input)))
print("Part 2: " + str(totalFuelRequired(input)))
