import re

with open("../input/day07.txt", "r") as file:
    lines = file.read().splitlines()

wires = {}

def find_wire(wire):
    for line in lines:
        parts = line.split(" -> ")

        if parts[1] == wire:
            return parts[0]

def calculate(wire):
    if re.match("\d+", wire):
        return int(wire)
    
    if wire in wires:
        return wires[wire]

    line = find_wire(wire)

    parts = line.split(" ")

    if len(parts) == 1:
        value = calculate(parts[0])
    elif len(parts) == 2:
        value = ~calculate(parts[1])
    elif len(parts) == 3:
        if parts[1] == "AND":
            value = calculate(parts[0]) & calculate(parts[2])
        elif parts[1] == "OR":
            value = calculate(parts[0]) | calculate(parts[2])
        elif parts[1] == "LSHIFT":
            value = calculate(parts[0]) << int(parts[2])
        elif parts[1] == "RSHIFT":
            value = calculate(parts[0]) >> int(parts[2])

    wires[wire] = value
    return value


wire_a_a = calculate("a")

wires = {"b": wire_a_a}

wire_a_b = calculate("a")

print("Wire \"a\": first iteration: {0}, second iteration: {1}".format(wire_a_a, wire_a_b))
