import re

line = open("../input/day12.txt", "r").read()

count = 0

numbers = re.findall(r"(-?\d+)", line)

for number in numbers:

    count += int(number)

while True:

    next_object = re.search(r"{([^{}]+)}", line)

    if not next_object:
        break

    next_object = next_object.group(1)

    if re.search(r":\"red\"", next_object):
        line = re.sub(r"({[^{}]+})", "RED", line, 1)
    else:
        line = re.sub(r"{([^{}]+)}", "(\\1)", line, 1)

non_red_count = 0

numbers = re.findall(r"(-?\d+)", line)

for number in numbers:

    non_red_count += int(number)

print("Part 1: Total: {0}.\nPart 2: Non-red total: {1}.".format(count, non_red_count))
