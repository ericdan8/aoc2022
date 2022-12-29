fs = {
    "name": "/",
    "contents": {},
    "parent": None
}

with open("input", "r") as f:
    lines = [l.strip() for l in f.readlines()]

i = 0
ptr = fs
while i < len(lines):
    line = lines[i]
    split_line = line.split()
    cmd = split_line[1]

    if cmd == "cd":
        target = split_line[2]
        if target == "/":
            ptr = fs
        elif target == "..":
            ptr = ptr["parent"]
        else:
            ptr = ptr["contents"][target]
    else:
        # ls
        j = i+1
        while j < len(lines) and lines[j][0] != "$":
            [a, b] = lines[j].split()
            if a == "dir":
                ptr["contents"][b] = {
                    "name": b,
                    "contents": {},
                    "parent": ptr
                }
            else:
                ptr["contents"][b] = {
                    "name": b,
                    "size": int(a)
                }
            j += 1

    i += 1

def print_fs(ptr, level=0):
    indentation = "  " * level
    if "contents" in ptr:
        print(f"{indentation}{ptr['name']} {ptr['size']}")
        for c in ptr["contents"].values():
            print_fs(c, level+1)
    else:
        print(f"{indentation}{ptr['name']} {ptr['size']}")


def compute_size(ptr):
    if "contents" in ptr:
        total_size = sum(compute_size(c) for c in ptr["contents"].values())
        ptr["size"] = total_size
        return total_size
    else:
        return ptr["size"]

compute_size(fs)
print_fs(fs)

30000000
smallest = 70000000
smallest_dir = ""

def visit(ptr, s=0):
    if "contents" in ptr:
        if ptr["size"] <= 100000:
            return ptr["size"] + sum(visit(c) for c in ptr["contents"].values())
        else:
            return sum(visit(c) for c in ptr["contents"].values())
    else:
        return 0

print(visit(fs))