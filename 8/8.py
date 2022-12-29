with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

visible = [[False for c in l] for l in lines]

trees = lines

for i, l in enumerate(trees):
    tallest = -1
    for j, c in enumerate(l):
        if int(c) > tallest:
            visible[i][j] = True
            tallest = int(c)

for i in list(range(len(trees)))[::-1]:
    l = trees[i]
    tallest = -1
    for j in list(range(len(l)))[::-1]:
        c = int(l[j])
        if c > tallest:
            visible[i][j] = True
            tallest = int(c)

for j in list(range(len(trees[0]))):
    tallest = -1
    for i in list(range(len(trees))):
        c = int(trees[i][j])
        if c > tallest:
            visible[i][j] = True
            tallest = int(c)

for j in list(range(len(trees[0])))[::-1]:
    tallest = -1
    for i in list(range(len(trees)))[::-1]:
        c = int(trees[i][j])
        if c > tallest:
            visible[i][j] = True
            tallest = int(c)

total = 0
for l in visible:
    for v in l:
        if v:
            total +=1

print(total)