sequence = "1113122113"

def look(sequence):

    runs = []

    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i - 1] == sequence[i]:
            count += 1
        else:
            runs += [sequence[i - 1] * count]
            count = 1

    runs += [sequence[len(sequence) - 1] * count]

    return runs

def look_and_say(sequence):

    new_sequence = ""

    runs = look(sequence)

    for run in runs:
        new_sequence += str(len(run)) + run[0]

    return new_sequence

for i in range(0, 40):
    sequence = look_and_say(sequence)

result = len(sequence)

for i in range(0, 10):
    sequence = look_and_say(sequence)

print("Part 1: First length: {0}.\nPart 2: Second length: {1}.".format(result, len(sequence)))
