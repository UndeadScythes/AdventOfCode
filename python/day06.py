import re

with open("../input/day06.txt", "r") as file:
    lines = file.read().splitlines()

lights = [[0 for x in range(1000)] for y in range(1000)]
brightness = [[0 for x in range(1000)] for y in range(1000)]

for line in lines:

    parts = line.split(" ")

    coordinate_a = parts[1]
    coordinate_b = parts[3]
    operation = "toggle"

    if len(parts) == 5:
        coordinate_a = parts[2]
        coordinate_b = parts[4]
        operation = parts[1]

    x_a = int(coordinate_a.split(",")[0])
    x_b = int(coordinate_b.split(",")[0])
    y_a = int(coordinate_a.split(",")[1])
    y_b = int(coordinate_b.split(",")[1])

    for x in range(x_a, x_b + 1):
        for y in range(y_a, y_b + 1):

            if operation == "toggle":
                lights[x][y] ^= 1
                brightness[x][y] += 2
            if operation == "on":
                lights[x][y] = 1
                brightness[x][y] += 1
            if operation == "off":
                lights[x][y] = 0
                if brightness[x][y] > 0:
                    brightness[x][y] -= 1

lights_on = 0
brightness_total = 0

for x in range(1000):
    for y in range(1000):
        
        lights_on += lights[x][y]
        brightness_total += brightness[x][y]

print("Part 1: {0} lights on.\nPart 2: Brightness: {1}.".format(lights_on, brightness_total))
