with open("input", "r") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

overlaps = 0

for l in lines:
    [s1, s2] = l.split(",")
    s1 = [int(w) for w in s1.split("-")]
    s2 = [int(w) for w in s2.split("-")]

    if s1[0] == s2[0]:
        overlaps += 1
    elif s1[0] < s2[0]:
        if s1[1] >= s2[0]:
            overlaps += 1
    else:
        if s2[1] >= s1[0]:
            overlaps += 1

print(overlaps)