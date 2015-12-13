import re

with open("../input/day08.txt", "r") as file:
    lines = file.read().splitlines()

string_count = 0
memory_count = 0
escaped_count = 0

for line in lines:
    string_count += len(line)
    
    memory_count += len(re.findall(r"(?:\\x\w{2}|\\\"|\\\\|\w)", line))

    line = "\"" + re.sub(r"(\\|\")", r"\\\1", line) + "\""
    
    escaped_count += len(line)

memory = string_count - memory_count
escaped_memory  = escaped_count - string_count

print("Memory: {0}, Escaped: {1}".format(memory, escaped_memory))
