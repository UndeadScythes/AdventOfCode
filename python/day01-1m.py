import functools
print("Final floor: {0}".format(functools.reduce((lambda f, i: f + (1 if i == "(" else -1)), open("../input/day01.txt", "r").read(), 0)))
