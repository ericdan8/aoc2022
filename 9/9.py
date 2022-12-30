with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0
visited = set()

for l in lines:
    d, n = l.split()
    for i in range(int(n)):
        if d == "R":
            head_x += 1
        elif d == "L":
            head_x -= 1
        elif d == "U":
            head_y += 1
        elif d == "D":
            head_y -= 1
        
        d_x = head_x - tail_x
        d_y = head_y - tail_y

        if abs(d_x) >= 2:
            dn = 1 if d_x > 0 else -1
            tail_x += dn
            tail_y = head_y
        elif abs(d_y) >= 2:
            dn = 1 if d_y > 0 else -1
            tail_y += dn
            tail_x = head_x
        
        visited.add((tail_x, tail_y))

print(len(visited))