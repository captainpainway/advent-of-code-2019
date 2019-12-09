instructions = list(map(int, open('day9input.txt').read().split(",")))
#instructions = [104,1125899906842624,99]
#instructions = [1102,34915192,34915192,7,4,7,99,0]
#instructions = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

def parseParameterModes(param):
    return {"opcode": param[-2:], "param1": param[2], "param2": param[1], "param3": param[0]}

def calculateParameterModes(i, pointer, parameter, offset):
        # 0 = position mode
        # 1 = immediate mode
        # 2 = relative mode
        p1 = pointer + 1
        p2 = pointer + 2
        if parameter == "0":
            print(i[p2])
            if i[p2] > len(i):
                return i[i[p2] % len(i)]
            else:
                return i[i[p2]]
        elif parameter == "1":
            return i[p2]
        elif parameter == "2":
            return i[i[p2 + offset]]

def intcodeComputer(i, inputsignal = 0, phase = 0, usePhase = False, position = 0):
    pointer = position
    parsed = parseParameterModes(str(i[pointer]).zfill(5))
    opcode = parsed["opcode"]
    offset = 0

    # If we're beyond the first loop, we've already used the phase input.
    if position != 0:
        phaseinput = True
    else:
        phaseinput = not usePhase

    while opcode != "99":
        p1 = pointer + 1
        p2 = pointer + 2
        p3 = pointer + 3

        # These only output a value
        if opcode == "03" or opcode == "04" or opcode == "09":
            if parsed["param3"] == "2":
                v = i[p1 + offset]
            else:
                v = i[p1]
            pointer = pointer + 2

            # Save input value to the position in the parameter (1 param)
            if opcode == "03":
                # Only use the phase input once. Second time we use the input signal.
                if phaseinput == True:
                    i[v] = inputsignal
                else:
                    i[v] = phase
                    phaseinput = True

            # Print the value of the parameter (1 param)
            if opcode == "04":
                # Now we have to return the pointer position for part 2.
                if v > len(i):
                    return (i[v % len(i)], pointer)
                else:
                    return (i[v], pointer)

            # Add to offset
            if opcode == "09":
                offset += int(i[v])
                
        else:
            v1 = calculateParameterModes(i, pointer, parsed["param1"], offset)
            v2 = calculateParameterModes(i, pointer, parsed["param2"], offset)

            # Output position of the calculated value
            if parsed["param3"] == "2":
                outputPosition = i[p3 + offset]
            else:
                outputPosition = i[p3]

            # Add input values, store in position of third param (3 params)
            if opcode == "01":
                i[outputPosition] = int(v1) + int(v2)
                pointer = pointer + 4

            # Multiply input values, store in position of third param (3 params)
            if opcode == "02":
                i[outputPosition] = int(v1) * int(v2)
                pointer = pointer + 4

            # If first param != 0, set pointer to second value (2 params)
            if opcode == "05":
                if int(v1) != 0:
                    pointer = int(v2)
                else:
                    pointer = pointer + 3

            # If first param == 0, set pointer to second value (2 params)
            if opcode == "06":
                if int(v1) == 0:
                    pointer = int(v2)
                else:
                    pointer = pointer + 3

            # If first param < second param, store 1 in position of third param (3 params)
            if opcode == "07":
                if v1 < v2:
                    i[outputPosition] = 1
                    pointer = pointer + 4
                else:
                    i[outputPosition] = 0
                    pointer = pointer + 4

            # If first param == second param, store 1 in position of third param (3 params)
            if opcode == "08":
                if v1 == v2:
                    i[outputPosition] = 1
                    pointer = pointer + 4
                else:
                    i[outputPosition] = 0
                    pointer = pointer + 4
            
        parsed = parseParameterModes(str(i[pointer]).zfill(5))
        opcode = parsed["opcode"]

def boostProgram():
    op4 = intcodeComputer(instructions, 1)
    print(op4)

# Answer 1102 is too low.
boostProgram()
