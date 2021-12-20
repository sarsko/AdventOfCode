with open("input.txt", "r") as f:
    algo, grid = f.read().split("\n\n")
    algo = ["0" if e == "." else "1" for e in algo]
    grid = {(i,j) : "0" if e == "." else "1"
            for i, l in enumerate(grid.split())
            for j, e in enumerate(l)}

adj = [(a, b) for a in range(-1,2) for b in range(-1,2)]

def doOnce(x, y, i):
    default = "0" if i % 2 == 0 else "1"
    s = [grid[(x+a, y+b)] if (x+a, y+b) in grid else default for a, b in adj]
    return algo[int("".join(s),2)]

neighs = lambda x: {(a+i, b+j) for a, b in x for i, j in adj}

des = {2, 50}
for i in range(max(des)):
    grid = {(x, y): doOnce(x, y, i) for x, y in neighs(grid)}
    if i+1 in des:
        print(sum(map(int, grid.values())))
