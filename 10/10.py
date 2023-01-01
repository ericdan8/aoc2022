with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

state = "READY"
cycle = 1
total_strength = 0
x = 1
i = 0
v = 0
image = ['.'] * 40 * 6

while i < len(lines) or state != "READY":
    # print(f"cycle {cycle} x {x}")
    if abs(((cycle-1) % 40) - x) <= 1:
        print("drawing")
        image[cycle-1] = "#"
    cycle += 1

    if state == "READY":
        line = lines[i].split()
        cmd = line.pop(0)
        if cmd == "addx":
            v = int(line.pop(0))
            state = "ADDING"
        i += 1
    elif state == "ADDING":
        x += v
        state = "READY"


for i in range(6):
    print("".join(image[i*40:(i+1)*40]))
