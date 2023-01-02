with open("input", "r") as f:
    rawl = [l.strip() for l in f.readlines()]
    m = [[c for c in l] for l in rawl]
blobm = "".join(rawl)
s_x = blobm.index("S") % len(m[0])
s_y = blobm.index("S") // len(m[0])
e_x = blobm.index("E") % len(m[0])
e_y = blobm.index("E") // len(m[0])

best = {}

def height(x, y):
    c = m[y][x]
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - 97

q = [(s_x, s_y)]

def get_best(x, y):
    if (x, y) not in best:
        best[(x, y)] = float("infinity")
    return best[(x, y)]

while q:
    [x, y] = q.pop(0)
    prev_best = get_best(x, y)
    c = m[y][x]
    h = height(x, y)
    prevs = []

    if y > 0 and h - height(x, y-1) <= 1:
        prevs.append(get_best(x, y-1))
    if y+1 < len(m) and h - height(x, y+1) <= 1:
        prevs.append(get_best(x, y+1))
    if x > 0 and h - height(x-1, y) <= 1:
        prevs.append(get_best(x-1, y))
    if x+1 < len(m[0]) and h - height(x+1, y) <= 1:
        prevs.append(get_best(x+1, y))

    # print(prevs)
    new_best = min(prevs) + 1 if c != "S" else 0
    if new_best < prev_best:
        best[(x, y)] = new_best
        if y > 0 and height(x, y-1) - h <= 1:
            q.append((x, y-1))
        if y+1 < len(m) and height(x, y+1) - h <= 1:
            q.append((x, y+1))
        if x > 0 and height(x-1, y) - h <= 1:
            q.append((x-1, y))
        if x+1 < len(m[0]) and height(x+1, y) - h <= 1:
            q.append((x+1, y))

for j in range(len(m)):
    # print("".join([ f"({m[j][i]}, {best[(i,j)] if (i,j) in best else -1})" for i in range(len(m[0])) ]))
    print("".join([ "," + m[j][i] + "{:0>3}".format(best[(i,j)] if (i,j) in best else -1) for i in range(len(m[0])) ]))

print(best[(e_x, e_y)])