with open("input", "r") as f:
    lines = f.readlines()

max_elf = 0

elves = [[]]

for l in lines:
    if l == "\n":
        elves.append([])
    else:
        elves[-1].append(int(l.strip()))

elves = [sum(e) for e in elves]

print(max(elves))