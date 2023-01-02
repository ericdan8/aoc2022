import json

with open("input", "r") as f:
    raw = f.read()

pairs = [[json.loads(l) for l in c.split("\n")] for c in raw.split("\n\n")]
idx_sum = 0

def ordered(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if right < left:
            return False
        if left == right:
            return None
    elif type(left) == list and type(right) == list:
        while left:
            if not right:
                return False
            l = left.pop(0)
            r = right.pop(0)
            result = ordered(l, r)
            if result is not None:
                return result
        if right:
            return True
        else:
            return None
    else:
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return ordered(left, right)

for i, p in enumerate(pairs):
    if ordered(p[0], p[1]):
        idx_sum += i + 1

print(idx_sum)