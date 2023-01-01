monkeys = []

with open("input", "r") as f:
    text = f.read()

raw_monkey_defs = text.split("\n\n")

for rmdef in raw_monkey_defs:
    lines = rmdef.split("\n")
    items = [int(n) for n in lines[1].split(":")[1].split(", ")]
    operation = lines[2].split(": new = ")[1]
    test = int(lines[3].split()[-1])
    targets = [int(lines[4].split()[-1]), int(lines[5].split()[-1])]

    monkey = {
        "items": items,
        "operation": operation,
        "test": test,
        "targets": targets
    }
    monkeys.append(monkey)

activity = [0] * len(monkeys)
for _ in range(20):
    # print([m['items'] for m in monkeys])
    for i, monkey in enumerate(monkeys):
        while monkey["items"]:
            item = monkey["items"].pop(0)
            item = eval(monkey["operation"].replace("old", str(item))) // 3
            activity[i] += 1
            if item % monkey["test"] == 0: 
                target = monkey["targets"][0]
            else:
                target = monkey["targets"][1]
            monkeys[target]["items"].append(item)

activity.sort()
print(activity[-1] * activity[-2])