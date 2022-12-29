with open("input", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

groups = [lines[i*3:(i*3)+3] for i in range(len(lines) // 3)]

score = 0
for g in groups:
    print(g)
    [x, y, z] = [set([c for c in e]) for e in g]

    common = x.intersection(y).intersection(z)
    print(common)
    common = common.pop()[0]

    if common.isupper():
        score += ord(common) - 38
    else:
        score += ord(common) - 96


print(score)