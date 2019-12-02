input = list(map(int, open('day2input.txt').read().split(",")))

def addInput(a, b):
    return a + b;

def multiplyInput(a, b):
    return a * b;

def restoreGravityAssist(key):
    vals = list(input)
    vals[1] = key[0]
    vals[2] = key[1]
    pointer = 0
    opcode = vals[pointer]
    while opcode != 99:
        vals1 = vals[vals[pointer + 1]]
        vals2 = vals[vals[pointer + 2]]
        outputPosition = vals[pointer + 3]

        if opcode == 1:
            vals[outputPosition] = addInput(vals1, vals2)

        if opcode == 2:
            vals[outputPosition] = multiplyInput(vals1, vals2)
        
        pointer = pointer + 4
        opcode = vals[pointer]
    return vals[0]

def findNounVerbValues():
    noun = 0
    while noun < 100:
        verb = 0
        while verb < 100:
            calculation = restoreGravityAssist((noun, verb))
            if calculation == 19690720:
                return 100 * noun + verb
            verb += 1
        noun += 1

print(restoreGravityAssist((12, 2)))
print(findNounVerbValues())
