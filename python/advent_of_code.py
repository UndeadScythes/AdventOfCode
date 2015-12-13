import os.path
import time

for i in range(1, 26):

    print("====== Advent of Code - Day {0} ======".format(i))

    day = "day{0:02}".format(i)
    part_1 = "{0}-1".format(day)
    part_2 = "{0}-2".format(day)

    day_exists = os.path.isfile("{0}.py".format(day))
    file_1_exists = os.path.isfile("{0}.py".format(part_1))
    file_2_exists = os.path.isfile("{0}.py".format(part_2))

    start = time.time()

    if file_1_exists and file_2_exists:
        exec(open("{0}.py".format(part_1)).read())
        exec(open("{0}.py".format(part_2)).read())
    elif day_exists:
        exec(open("{0}.py".format(day)).read())
    else:
        print("No solution for Day {0}.".format(i))

    print("Time taken: {0}ms".format(round((time.time() - start) * 1000)))
