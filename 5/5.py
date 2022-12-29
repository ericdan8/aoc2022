crates = None
num_stacks = 0
with open("input", "r") as f:
    while True:
        line = f.readline()
        if crates is None:
            crates = [[] for i in range(len(line) // 4)]
            num_stacks = len(line) // 4

        if all(w.isnumeric() for w in line.split()):
            num_stacks = int(line.split()[-1])
            break
        else:
            # populate stacks
            for i in range(num_stacks):
                crate = line[(i * 4) + 1]
                if crate != " ":
                    crates[i].insert(0, crate)
    f.readline()
    instructions = [l.strip() for l in f.readlines()]

print(instructions)

for i in instructions:
    s = i.split()
    repeats = int(s[1])
    f = int(s[3])
    t = int(s[5])

    # print(f"moving {repeats} from {f} to {t}")
    for j in range(repeats):
        c = crates[f-1].pop()
        crates[t-1].append(c)

print("".join(s[-1] for s in crates))