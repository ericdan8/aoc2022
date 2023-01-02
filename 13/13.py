import json
import functools

with open("input", "r") as f:
    raw = f.read()

packets = [json.loads(l) for l in raw.replace("\n\n", "\n").split("\n")]
print(packets)
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
        i = 0
        while i < len(left):
            if i >= len(right):
                return False
            l = left[i]
            r = right[i]
            result = ordered(l, r)
            if result is not None:
                return result
            i += 1
        if i < len(right):
            return True
        else:
            return None
    else:
        if type(left) == int:
            left = [left]
        else:
            right = [right]
        return ordered(left, right)

packets += [[[2]], [[6]]]
packets.sort(key=functools.cmp_to_key(lambda l, r: -1 if ordered(l,r) else 1))

# for p in packets:
#     print(p)


print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))