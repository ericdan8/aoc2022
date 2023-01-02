with open("input", "r") as f:
    rawl = [l.strip() for l in f.readlines()]
    m = [[c for c in l] for l in rawl]
blobm = "".join(rawl)
s_x = blobm.index("S") % len(m[0])
s_y = blobm.index("S") // len(m[0])

best = {}

def height(x, y):
    c = m[y][x]
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - 97

def explore(x, y, indent = "", path = []):
    print(f'{indent}exploring {(x, y)}')
    if (x, y) in best:
        return best[(x, y)]

    c = m[y][x]
    h = height(x, y)
    if c == "E":
        best[(x, y)] = 0
        return 0
    best[(x, y)] = float("infinity")
    paths = []
    if y > 0 and height(x, y-1) - h <= 1:
        # print(f"{indent}{x,y}exploring up:")
        paths.append(1 + explore(x, y-1, indent + "  ", path + [(x, y)]))
    if y+1 < len(m) and height(x, y+1) - h <= 1:
        # print(f"{indent}{x,y}exploring down:")
        paths.append(1 + explore(x, y+1, indent + "  ", path + [(x, y)]))
    if x > 0 and height(x-1, y) - h <= 1:
        # print(f"{indent}{x,y}exploring left:")
        paths.append(1 + explore(x-1, y, indent + "  ", path + [(x, y)]))
    if x+1 < len(m[0]) and height(x+1, y) - h <= 1:
        # print(f"{indent}{x,y}exploring right:")
        paths.append(1 + explore(x+1, y, indent + "  ", path + [(x, y)]))

    best[(x, y)] = min(paths) if paths else float("infinity")
    # if c == "S":
    #     print(path)
    return min(paths) if paths else float("infinity")
    
print(s_x)
print(s_y)
print(explore(s_x, s_y))
for j in range(len(m)):
    # print("".join([ f"({m[j][i]}, {best[(i,j)] if (i,j) in best else -1})" for i in range(len(m[0])) ]))
    print("".join([ "," + m[j][i] + "{:0>3}".format(best[(i,j)] if (i,j) in best else -1) for i in range(len(m[0])) ]))