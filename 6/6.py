with open("input", "r") as f:
    msg = f.readlines()[0].strip()

for i in range(len(msg)):
    print(f"checking {msg[i:i+14]}")
    if len(set(char for char in msg[i:i+14])) == 14:
        print(i+14)
        break