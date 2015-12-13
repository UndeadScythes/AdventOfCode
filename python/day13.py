from itertools import permutations

with open("../input/day13.txt", "r") as file:
    lines = file.read().splitlines()

happiness = 0

guests = []

for line in lines:

    parts = line.split(" ")

    guest_a = parts[0]
    guest_b = parts[10].rstrip(".")

    if not guest_a in guests:
        guests += [guest_a]
    if not guest_b in guests:
        guests += [guest_b]

guests += ["Me"]

guest_count = len(guests)

gains = [[0 for x in range(guest_count)] for y in range(guest_count)]

for line in lines:

    parts = line.split(" ")

    a = guests.index(parts[0])
    b = guests.index(parts[10].rstrip("."))

    gain = int(parts[3])

    if parts[2] == "lose":
        gain = -gain

    gains[a][b] = gain

layouts = permutations([i for i in range(guest_count)])

for layout in layouts:

    test_happiness = 0
    
    for i in range(len(layout)):
        next_i = (i + 1) % guest_count
        
        test_happiness += gains[layout[i]][layout[next_i]]
        test_happiness += gains[layout[next_i]][layout[i]]

    if test_happiness > happiness:
        happiness = test_happiness

print("Part 2: Optimal happiness: {0}.".format(happiness))
