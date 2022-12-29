with open("input", "r") as f:
    trees = [[int(c) for c in l.strip()] for l in f.readlines()]

print(trees)

def compute_scenery(y, x):
    height = trees[y][x]
    left = 0
    right = 0
    up = 0
    down = 0

    # left
    i = x-1
    while i >= 0:
        left += 1
        if (trees[y][i]) >= height:
            break
        i -= 1
        
    # right
    i = x+1
    while i < len(trees[0]):
        right += 1
        if (trees[y][i]) >= height:
            break
        i += 1

    # up
    i = y-1
    while i >= 0:
        up += 1
        if (trees[i][x]) >= height:
            break
        i -= 1

    # down
    i = y+1
    while i < len(trees):
        down += 1
        if (trees[i][x]) >= height:
            break
        i += 1

    return left * right * up * down

print(max(compute_scenery(i, j) for i in range(len(trees)) for j in range(len(trees[0]))))
# print(compute_scenery(3, 2))