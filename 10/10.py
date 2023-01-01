with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

state = "READY"
cycle = 1
total_strength = 0
x = 1
i = 0
v = 0

while i < len(lines) or state != "READY":
    print(f"cycle {cycle} x {x}")
    if ((cycle - 20) % 40) == 0:
        print(f"ADDING cycle {cycle} x {x}")
        total_strength += (cycle) * x
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
print(f"cycle {cycle} x {x}")
    
print(total_strength)