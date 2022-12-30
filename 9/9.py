with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

rope_x = [0] * 10
rope_y = [0] * 10
visited = set()

for l in lines:
    d, n = l.split()
    # print(f"{d} {n}")
    for i in range(int(n)):
        # print(d)
        if d == "R":
            rope_x[0] += 1
        elif d == "L":
            rope_x[0] -= 1
        elif d == "U":
            rope_y[0] += 1
        elif d == "D":
            rope_y[0] -= 1
        
        for j in range(1, len(rope_x)):
            ahead_x = rope_x[j-1]
            ahead_y = rope_y[j-1]

            d_x = ahead_x - rope_x[j]
            d_y = ahead_y - rope_y[j]

            if abs(d_x) >= 2 or abs(d_y) >= 2:
                dn_x = d_x // (abs(d_x) if abs(d_x) > 0 else 1)
                dn_y = d_y // (abs(d_y) if abs(d_y) > 0 else 1)
                rope_x[j] += dn_x
                rope_y[j] += dn_y
            # elif abs(d_y) >= 2:
            #     dn = 1 if d_y > 0 else -1
            #     rope_y[j] += dn
            #     rope_x[j] = ahead_x
            
        visited.add((rope_x[-1], rope_y[-1]))
        

print(len(visited))