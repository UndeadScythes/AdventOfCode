with open("../input/day02.txt", "r") as file:
    lines = file.read().splitlines()

area   = 0
ribbon = 0

for line in lines:

    dims = list(map(lambda x: int(x), line.split("x")))
    dims.sort()

    area += 3 * dims[0] * dims[1]
    area += 2 * dims[0] * dims[2]
    area += 2 * dims[1] * dims[2]

    ribbon += 2 * (dims[0] + dims[1])
    ribbon += dims[0] * dims[1] * dims[2]

print("Area: {0}, Ribbon: {1}".format(area, ribbon))
