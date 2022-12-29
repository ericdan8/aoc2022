with open("input", "r") as f:
    lines = f.readlines()


def shape_score(shape):
    if shape == "X":
        return 1
    if shape == "Y":
        return 2
    if shape == "Z":
        return 3

draws = { ("A", "X"), ("B", "Y"), ("C", "Z") }
wins = { ("A", "Y"), ("B", "Z"), ("C", "X") }

def round_score(opponent, me):
    if (opponent, me) in draws:
        return 3
    if (opponent, me) in wins:
        return 6
    return 0

score = 0

for l in lines:
    (opponent, me) = l.split()
    score += shape_score(me)
    score += round_score(opponent, me)

print(score)