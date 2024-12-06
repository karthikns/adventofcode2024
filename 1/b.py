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

mDict = dict()
for num in m:
    if num not in mDict:
        mDict[num] = 0
    mDict[num] += 1

accum = 0
for num in n:
    if num in mDict:
        accum += num * mDict[num]

print(accum)