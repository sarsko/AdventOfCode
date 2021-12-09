grid = [list(map(int, l.strip())) for l in open("input.txt", "r").readlines()]
w = len(grid[0]); h = len(grid)

valid_neighs = lambda i, j: {(min(i+1, h-1), j), (max(i-1, 0), j), (i, min(j+1, w-1)), (i, max(j-1, 0))} - {(i,j)}
check = lambda i, j, grid: all(grid[i][j] < grid[i2][j2] for i2, j2 in valid_neighs(i, j))

lps = {(i,j) for i, l in enumerate(grid) for j, _ in enumerate(l) if check(i, j, grid)}
print(sum(grid[i][j] + 1 for i, j in lps))

calc_basin = lambda i, j, grid : {(i,j)} | { bas for i2, j2 in valid_neighs(i, j) for bas in (calc_basin(i2, j2, grid) if grid[i][j] < grid[i2][j2] < 9 else ()) }
basins = sorted([len(calc_basin(i, j, grid)) for i, j in lps])
print(basins[-1]*basins[-2]*basins[-3])
