f = open("input.txt", "r")
l1 = f.readline().strip().split(",")
l2 = f.readline().strip().split(",")
seen = set()
crosses = set()
stepmap = {}
up = 0
right = 0
steps = 0
for e in l1:
    if e[0] == "U":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            up += 1
            seen.add((up, right))
            stepmap[(up,right)] = steps
    elif e[0] == "D":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            up -= 1
            seen.add((up, right))
            stepmap[(up,right)] = steps
    elif e[0] == "R":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            right += 1
            seen.add((up, right))
            stepmap[(up,right)] = steps
    elif e[0] == "L":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            right -= 1
            seen.add((up, right))
            stepmap[(up,right)] = steps
up = 0
right = 0
steps = 0
min_crosses = 2147000000
for e in l2:
    if e[0] == "U":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            up += 1
            if (up, right) in seen:
                crosses.add((up, right))
                combined_steps = stepmap[(up, right)] + steps
                if combined_steps < min_crosses:
                    min_crosses = combined_steps
    elif e[0] == "D":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            up -= 1
            if (up, right) in seen:
                crosses.add((up, right))
                combined_steps = stepmap[(up, right)] + steps
                if combined_steps < min_crosses:
                    min_crosses = combined_steps
    elif e[0] == "R":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            right += 1
            if (up, right) in seen:
                crosses.add((up, right))
                combined_steps = stepmap[(up, right)] + steps
                if combined_steps < min_crosses:
                    min_crosses = combined_steps
    elif e[0] == "L":
        inc = int(e[1:])
        for i in range(inc):
            steps += 1
            right -= 1
            if (up, right) in seen:
                crosses.add((up, right))
                combined_steps = stepmap[(up, right)] + steps
                if combined_steps < min_crosses:
                    min_crosses = combined_steps
minimum = 2147000000
for (u, r) in crosses:
    if abs(u) + abs(r) < minimum:
        minimum = abs(u) + abs(r)
print(minimum)
print(min_crosses)
