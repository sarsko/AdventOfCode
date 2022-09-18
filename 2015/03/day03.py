inp = open("input.txt").read().strip()
x = 0
y = 0
pres = {}
pres[(0,0)] = 1
for e in inp:
    if e == ">":
        x += 1
    elif e == "<":
        x -= 1
    elif e == "^":
        y -= 1
    elif e == "v":
        y += 1
    pres[(x,y)] = 1
print(len(pres))

x = 0
y = 0
rx = 0
ry = 0
pres = {}
pres[(0,0)] = 1
for i, e in enumerate(inp):
    if i % 2 == 0:
        if e == ">":
            x += 1
        elif e == "<":
            x -= 1
        elif e == "^":
            y -= 1
        elif e == "v":
            y += 1
    else:
        if e == ">":
            rx += 1
        elif e == "<":
            rx -= 1
        elif e == "^":
            ry -= 1
        elif e == "v":
            ry += 1
    pres[(x,y)] = 1
    pres[(rx,ry)] = 1

print(len(pres))
