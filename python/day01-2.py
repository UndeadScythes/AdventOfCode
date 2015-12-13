instructions = open("../input/day01.txt", "r").read()

floor    = 1
basement = -1

for i in range(len(instructions)):
    
    if instructions[i] == "(":
        floor += 1
    if instructions[i] == ")":
        floor -= 1

    if floor == -1 and basement == -1:
        
        basement = i + 1
        
print("Part 2: Position {0}.".format(basement))
