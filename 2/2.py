with open("input", "r") as f:
    lines = f.readlines()


def shape_score(shape):
    if shape == "A":
        return 1
    if shape == "B":
        return 2
    if shape == "C":
        return 3

draws = { 
    "A": "A",
    "B": "B",
    "C": "C"
}

wins = { "A": "B", "B": "C", "C": "A" }

losses = { "A": "C", "B": "A", "C": "B" }

def round_score(opponent, result):
    if result == "X":
        return 0 + shape_score(losses[opponent])
    if result == "Y":
        return 3 + shape_score(draws[opponent])
    if result == "Z":
        return 6 + shape_score(wins[opponent])

score = 0

for l in lines:
    (opponent, result) = l.split()
    score += round_score(opponent, result)

print(score)