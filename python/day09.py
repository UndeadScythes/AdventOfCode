from itertools import permutations

with open("../input/day09.txt", "r") as file:
    lines = file.read().splitlines()

short_route = -1
long_route = 0

locations = []

for line in lines:

    parts = line.split(" ")

    if not parts[0] in locations:
        locations += [parts[0]]
    if not parts[2] in locations:
        locations += [parts[2]]

distances = [[0 for x in range(len(locations))] for y in range(len(locations))]

for line in lines:

    parts = line.split(" ")

    a = locations.index(parts[0])
    b = locations.index(parts[2])

    distance = int(parts[4])

    distances[a][b] = distance
    distances[b][a] = distance

orderings = permutations([i for i in range(len(locations))])

for ordering in orderings:

    test_route = 0
    
    for i in range(len(ordering) - 1):
        test_route += distances[ordering[i]][ordering[i + 1]]

    if test_route < short_route or short_route == -1:
        short_route = test_route
    if test_route > long_route:
        long_route = test_route
        

print("Shortest route: {0}, Longest route: {1}".format(short_route, long_route))
