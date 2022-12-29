with open("input", "r") as f:
    lines = f.readlines()

score = 0
for l in lines:
    l = l.strip()
    x = set(c for c in l[:len(l) // 2])
    y = set(c for c in l[len(l) // 2:])
    common = x.intersection(y)
    common = common.pop()[0]

    if common.isupper():
        score += ord(common) - 38
    else:
        score += ord(common) - 96


print(score)