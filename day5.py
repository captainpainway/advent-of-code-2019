# Program will prompt for input. Use 1 for first puzzle and 5 for the second.

instructions = list(map(int, open('day5input.txt').read().split(",")))
value = input("Input diagnostic ID: ")

def parseParameterModes(param):
    return {"opcode": param[-2:], "param1": param[2], "param2": param[1], "param3": param[0]}

def intcodeComputer(input, i):
    pointer = 0
    parsed = parseParameterModes(str(i[pointer]).zfill(5))
    opcode = parsed["opcode"]
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
                i[v] = input

            # Print the value of the parameter (1 param)
            if opcode == "04":
                print("Test result: " + str(i[v]))
                
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

intcodeComputer(value, instructions)
