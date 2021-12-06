f = open("input.txt", "r").read()
i = 0
nest = 0
score = 0
ingarb = False
garbScore = 0
while i < len(f):
    c = f[i]
    if c == "!":
        i += 1
    elif c == ">":
        ingarb = False
    elif ingarb:
        garbScore += 1
    else:
        if c == "<":
            ingarb = True
        elif c == "{":
            nest += 1
        elif c == "}":
           score += nest
           nest -= 1
    i += 1
print(score)
print(garbScore)
