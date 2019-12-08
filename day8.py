from collections import Counter

pixels = list(map(int, open('day8input.txt').read().strip()))
columns = 25
rows = 6

## PART 1 ##

# We're not going to worry about rows, just read each layer as a list.
layers = list(pixels[i: i + (columns * rows)] for i in range(0, len(pixels), columns * rows))

fz = None
for l in layers:
    # Use collections.Counter to get an object of character counts.
    count = Counter(l)
    if fz == None or count[0] < fz[0]:
        fz = count

print("Multiplied ones and twos: " + str(fz[1] * fz[2]))

## PART 2 ##

# Initialize an array of all "transparent" pixels.
fl = [2] * (columns * rows)
for l in layers:
    for i in range(0, len(l)):
        if fl[i] == 2:
            fl[i] = l[i]

# I want to replace the 1s and 0s with blocks to create a readable image.
fl = list(map(str, fl))
fl = [f.replace('0', '█').replace('1', '░') for f in fl]

# Chunk the final layer into rows and print.
image = list(fl[i: i + columns] for i in range(0, len(fl), columns))
print("Final image: ")
for row in image:
    print(''.join(row))
