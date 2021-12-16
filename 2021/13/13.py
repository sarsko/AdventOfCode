folds = []
coords = set()
with open("input.txt", "r") as f:
    for l in f:
        l = l.strip()
        if not l:
            continue
        if l[0] == "f":
            k, v = (*l[11:].split("="),)
            folds.append((k, int(v)))
        else:
            coords.add(map(int, (*l.split(","),)))

for i, (ax, pos) in enumerate(folds):
    new = set()
    if ax == "x":
        for x, y in coords:
            if x < pos:
                new.add((x,y))
            else:
                new.add((pos-(x-pos),y))
    else:
        for x, y in coords:
            if y < pos:
                new.add((x,y))
            else:
                new.add((x,pos-(y-pos)))
    coords = new
    if i == 0:
        print(len(coords))

for i in range(max(coords, key=lambda x:x[1])[1] + 1):
    for j in range(max(coords, key=lambda x:x[0])[0] + 1):
        if (j, i) in coords:
            print("X", end="")
        else:
            print(" ", end="")
    print()
