instructions = list(map(int, open('day5input.txt').read().split(",")))

def addInput(a, b):
    return int(a) + int(b);

def multiplyInput(a, b):
    return int(a) * int(b);

def parseParameterModes(param):
    return {"opcode": param[-2:], "param1": param[2], "param2": param[1], "param3": param[0]}

def intcodeComputer(input, instructions):
    vals = list(instructions)
    pointer = 0
    instructions = parseParameterModes(str(vals[pointer]).zfill(5))
    opcode = instructions["opcode"]
    while opcode != "99":
        if opcode == "01" or opcode == "02":
            if instructions["param1"] == "0":
                vals1 = vals[vals[pointer + 1]]
            else:
                vals1 = vals[pointer + 1]
            if instructions["param2"] == "0":
                vals2 = vals[vals[pointer + 2]]
            else:
                vals2 = vals[pointer + 2]

            outputPosition = vals[pointer + 3]
            pointer = pointer + 4

            if opcode == "01":
                vals[outputPosition] = addInput(vals1, vals2)

            if opcode == "02":
                vals[outputPosition] = multiplyInput(vals1, vals2)

        if opcode == "03" or opcode == "04":
            val = vals[pointer + 1]
            pointer = pointer + 2

            if opcode == "03":
                vals[val] = input

            if opcode == "04":
                print("Test result: " + str(vals[val]))
        
        instructions = parseParameterModes(str(vals[pointer]).zfill(5))
        opcode = instructions["opcode"]
    return vals[0]

intcodeComputer(1, instructions)
