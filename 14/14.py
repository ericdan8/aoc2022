g = {}
min_x = float("infinity")
max_x = float("-infinity")
highest = float("-infinity")
with open("input", "r") as f:
    for l in f:
        points = [ list(map(int, p.split(","))) for p in l.strip().split(" -> ") ]
        g[(points[0][0], points[0][1])] = "#"
        if points[0][1] > highest:
            highest = points[0][1]
        if points[0][0] < min_x:
            min_x = points[0][0]
        if points[0][0] > max_x:
            max_x = points[0][0]


        for i in range(1, len(points)):
            prev = points[i-1]
            p = points[i]
            v_x = (p[0] - prev[0]) // abs(p[0] - prev[0]) if p[0] - prev[0] != 0 else 0
            v_y = (p[1] - prev[1]) // abs(p[1] - prev[1]) if p[1] - prev[1] != 0 else 0
            ptr_x = prev[0]
            ptr_y = prev[1]

            while [ptr_x, ptr_y] != p:
                ptr_x += v_x
                ptr_y += v_y
                g[(ptr_x, ptr_y)] = "#"
                if ptr_y > highest:
                    highest = ptr_y
                if points[0][0] < min_x:
                    min_x = points[0][0]
                if points[0][0] > max_x:
                    max_x = points[0][0]


sands = 0
def drop_sand():
    s_x = 500
    s_y = 0
    while True:
        if s_y + 1 == highest + 2:
            g[(s_x,s_y)] = "o"
            break
        if (s_x, s_y+1) in g:
            if (s_x-1, s_y+1) in g:
                if (s_x+1, s_y+1) in g:
                    g[(s_x,s_y)] = "o"
                    break
                else:
                    s_x += 1
            else:
                s_x -= 1
        s_y += 1
    return (s_x, s_y) == (500, 0)

def show():
    for j in range(0, highest+4):
        l = "{:0>3}".format(j)
        for i in range(min_x-5,max_x+5):
            if (i,j) in g:
                l += g[(i,j)]
            else:
                # if i == 500:
                #     l += "~"
                # elif i % 10 == 0:
                #     l += "|"
                # elif i % 5 == 0:
                #     l += "`"
                # else:
                l += "."
        print(l)
while True:
    # print("dropping")
    sands += 1
    if drop_sand():
        break
show()
    
print(sands)