input = open('day3input.txt').read().splitlines()

# Yes, these globals are nasty
line1 = input[0].split(',')
line2 = input[1].split(',')
l1coords = (0, 0)
l2coords = (0, 0)
l1set = set()
l2set = set()
step1 = 0
step2 = 0
dict1 = {}
dict2 = {}

# Create sets (for part 1) and dictionaries (for part 2)
def tracelines(line, thisset, coords, step, thisdict):
    for l in line:
        amount = l[1:]
        for i in range(0, int(amount)):
            step += 1
            if l[0] == 'R':
                coords = (coords[0] + 1, coords[1])
            if l[0] == 'U':
                coords = (coords[0], coords[1] + 1)
            if l[0] == 'L':
                coords = (coords[0] - 1, coords[1])
            if l[0] == 'D':
                coords = (coords[0], coords[1] - 1)
            thisset.add(coords)
            thisdict[coords] = step

tracelines(line1, l1set, l1coords, step1, dict1)
tracelines(line2, l2set, l2coords, step2, dict2)

# This is where our lines cross
crosses = l1set.intersection(l2set)

# Make an array of distances and sort for part 1
distance = []
for c in crosses:
    distance.append(abs(c[0]) + abs(c[1]))

distance.sort()

print("Closest intersection: " + str(distance[0]))

# Where we have a cross, get the steps to get there and add to array for part 2
steps = []
for c in crosses:
    steps.append(dict1[c] + dict2[c])

steps.sort()
print("Best steps: " + str(steps[0]))
