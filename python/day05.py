import re

with open("../input/day05.txt", "r") as file:
    lines = file.read().splitlines()

niceStrings_v1 = 0

niceStrings_v2 = 0

for line in lines:

    if not re.search(r"(?:ab|cd|pq|xy)", line) and re.search(r"([a-z])\1", line) and len(re.findall(r"[aeiou]", line)) >= 3:
        niceStrings_v1 += 1

    if re.search(r"([a-z]{2})[a-z]*\1", line) and re.search(r"([a-z])[a-z]\1", line):
        niceStrings_v2 += 1
    
print("Part 1: {0} nice strings.".format(niceStrings_v1))
print("Part 2: {0} nice strings.".format(niceStrings_v2))
