pos = 50
p1 = 0
p2 = 0
pos_was_0 = False

for l in open("input.txt").read().split():
    v = int(l[1:])
    op = int.__sub__ if l[0] == "L" else int.__add__
    pos = op(pos, v)

    while pos < 0:
        pos += 100
        if not pos_was_0: 
            p2 += 1
        pos_was_0 = False

    while pos >= 100:
        pos -= 100
        # Will be counted below
        if pos != 0:
            p2 += 1

    pos_was_0 = False
    if pos == 0:
        p1 += 1
        pos_was_0 = True
        p2 += 1

print(p1)
print(p2)
