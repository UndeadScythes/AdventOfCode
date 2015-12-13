instructions = open("../input/day03.txt", "r").read()

location = [[0, 0], [0, 0]]
visited  = [[0, 0]]

for i in range(len(instructions)):

    robo = i % 2

    if instructions[i] == "^":
        location[robo][1] += 1
    if instructions[i] == "v":
        location[robo][1] -= 1
    if instructions[i] == "<":
        location[robo][0] -= 1
    if instructions[i] == ">":
        location[robo][0] += 1

    newLocation = True

    for coordinates in visited:
        if coordinates[0] == location[robo][0] and coordinates[1] == location[robo][1]:
            newLocation = False
            break

    if newLocation:
        visited += [[location[robo][0], location[robo][1]]]
        
print("Part 2: {0} houses visited.".format(len(visited)))
