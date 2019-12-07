orbits = open('day6input.txt').read().splitlines()
orbiting = {}

# Make the orbiter the key and the orbitee the value,
# that way we can work backwards to the root.
def mapOrbits(o):
    split = o.split(')')
    orbiting[split[1]] = split[0]

# Work backward from each node to "COM" and add it up.
def countOrbits(t):
    length = 0
    for i in t:
        length += 1
        current = t[i]
        while current != "COM":
            length += 1
            current = t[current]
    print("Number of orbits: " + str(length))

# This is obnoxious.
# Work backward from "YOU" to "COM" and then "SAN" to "COM".
# Then, flip those lists around and loop through the duplicates,
# remove the dups except for the last one (shared along the path).
# Finally, work backward from "YOU" to the shared ancestor,
# and from "SAN" to the same ancestor.
def santaDistance(t):
    youToCom = []
    current = t["YOU"]
    while current != "COM":
        youToCom.append(current)
        current = t[current]

    sanToCom = []
    current = t["SAN"]
    while current != "COM":
        sanToCom.append(current)
        current = t[current]

    # Finding the dupes and removing the shared ancestor.
    youToCom.reverse()
    sanToCom.reverse()
    dupes = []
    for i, name in enumerate(sanToCom):
        if name == youToCom[i]:
            dupes.append(name)
    shared = dupes.pop()

    # Looping through the path from "YOU" to "SAN".
    youToShared = []
    current = t["YOU"]
    while current != shared:
        youToShared.append(current)
        current = t[current]

    sanToShared = []
    current = t["SAN"]
    while current != shared:
        sanToShared.append(current)
        current = t[current]

    print("Orbits to Santa: " + str(len(youToShared + sanToShared)))
    

list(map(mapOrbits, orbits))

countOrbits(orbiting)

santaDistance(orbiting)
