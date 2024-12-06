import re

lines = None
with open("1/input") as file:
    lines = file.readlines()

pattern = re.compile(r"(\d+)\s+(\d+)", re.VERBOSE)

n = []
m = []
for line in lines:
    match = pattern.match(line)
    n.append(int(match.group(1)))
    m.append(int(match.group(2)))

assert len(n) == len(m)

n.sort()
m.sort()

accum = 0
for index in range(len(n)):
    accum += abs(n[index] - m[index])

print(accum)