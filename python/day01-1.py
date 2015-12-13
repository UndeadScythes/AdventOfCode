instructions = open("../input/day01.txt", "r").read()

floor = 0

for i in range(len(instructions)):
    
    if instructions[i] == "(":
        floor += 1
    if instructions[i] == ")":
        floor -= 1

print("Part 1: Floor {0}.".format(floor))
