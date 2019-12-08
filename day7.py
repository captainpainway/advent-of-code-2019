from itertools import permutations

instructions = list(map(int, open('day7input.txt').read().split(",")))

def parseParameterModes(param):
    return {"opcode": param[-2:], "param1": param[2], "param2": param[1], "param3": param[0]}

def intcodeComputer(phase, inputsignal, i, position = 0):
    pointer = position
    parsed = parseParameterModes(str(i[pointer]).zfill(5))
    opcode = parsed["opcode"]

    # If we're beyond the first loop, we've already used the phase input.
    if position != 0:
        phaseinput = True
    else:
        phaseinput = False

    while opcode != "99":
        p1 = pointer + 1
        p2 = pointer + 2
        p3 = pointer + 3

        # These only output a value
        if opcode == "03" or opcode == "04":
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
                return (i[v], pointer)
                
        else:
            # Calculate parameter modes
            # 0 = position mode
            # 1 = immediate mode
            if parsed["param1"] == "0":
                v1 = i[i[p1]]
            else:
                v1 = i[p1]
            if parsed["param2"] == "0":
                v2 = i[i[p2]]
            else:
                v2 = i[p2]

            # Output position of the calculated value
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

def amplificationCircuit():
    # Get all the permutations of the phases.
    possiblephases = list(permutations([0,1,2,3,4]))
    thrustlist = []
    for phases in possiblephases:
        inputsignal = 0
        for phase in phases:
            instcopy = instructions.copy()
            op4 = intcodeComputer(phase, inputsignal, instcopy)
            inputsignal = op4[0]
        thrustlist.append(int(inputsignal))

    # Get the highest number in the list
    thrustlist.sort(reverse=True)
    print("Amplification circuit highest signal: " + str(thrustlist[0]))

def feedbackLoop():
    possiblephases = list(permutations([5,6,7,8,9]))
    thrustlist = []
    for phases in possiblephases:
        # For each phase we need new positions and "computers" for each amp.
        # We don't want these overwritten as we're looping through.
        # We're going to append the position each time to the list and
        # jump back 5 places instead of keeping track of positions individually.
        positions = [0,0,0,0,0]
        end = False
        inputsignal = 0
        computerA = instructions.copy()
        computerB = instructions.copy()
        computerC = instructions.copy()
        computerD = instructions.copy()
        computerE = instructions.copy()
        # Put amp computers into a dictionary so we can access by index.
        comps = {0: computerA, 1: computerB, 2: computerC, 3: computerD, 4: computerE}
        while end == False:
            for (amp, phase) in enumerate(phases):
                op4 = intcodeComputer(phase, inputsignal, comps[amp], positions[-5])
                # If opcode 4 returns None, we seem to be finished, so append the signal
                # to thrustlist for sorting.
                if op4 == None:
                    end = True
                    thrustlist.append(int(inputsignal))
                    break
                else:
                    inputsignal = op4[0]
                    positions.append(op4[1])

    thrustlist.sort(reverse=True)
    print("Amplifier feedback loop highest signal: " + str(thrustlist[0]))
    
amplificationCircuit()
feedbackLoop()
