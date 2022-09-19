grid = [[0 for _ in range(102)] for _ in range(102)]
for i, l in enumerate(open("input.txt").read().strip().split("\n")):
    for j, e in enumerate(l):
        if e == "#":
            grid[i+1][j+1] = 1

    # Part 2
    grid[1][1] = 1
    grid[100][1] = 1
    grid[1][100] = 1
    grid[100][100] = 1

for s in range(100):
    newgrid = [[0 for _ in range(102)] for _ in range(102)]
    # cell is i+1 j+1
    for i in range(100):
        for j in range(100):
            neighs = grid[i][j] + grid[i][j+1] + grid[i][j+2]
            neighs += grid[i+1][j] + grid[i+1][j+2]
            neighs += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
            if neighs == 3 or neighs == 2 and grid[i+1][j+1]:
                newgrid[i+1][j+1] = 1
            else:
                newgrid[i+1][j+1] = 0

    grid = newgrid

    # Part 2
    grid[1][1] = 1
    grid[100][1] = 1
    grid[1][100] = 1
    grid[100][100] = 1

print(sum(sum(grid, [])))


