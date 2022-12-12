import sys
sys.setrecursionlimit(10000)

alf = "abcdefghijklmnopqrstuvwxyz"
grid = []
for i, line in enumerate(open("input.txt").read().strip().split("\n")):
    curr = []
    for j, c in enumerate(line):
        if c == "S":
            start = (i, j)
            c = "a"
        elif c == "E":
            end = (i, j)
            c = "z"
        curr.append(alf.index(c))
    grid.append(curr)

lengths = [[999 for _ in range(len(grid[0]))] for _ in range(len(grid))]

def calc(i, j, curr, grid, lengths):
    if curr > 440 or curr >= lengths[i][j]:
        return
    if curr < lengths[i][j]:
        lengths[i][j] = curr
    if i > 0 and grid[i][j] - grid[i-1][j] >= -1:
        calc(i - 1, j, curr + 1, grid, lengths)
    if i + 1 < len(grid) and grid[i][j] - grid[i+1][j] >= -1:
        calc(i + 1, j, curr + 1, grid, lengths)
    if j > 0 and grid[i][j] - grid[i][j-1] >= -1:
        calc(i, j - 1, curr + 1, grid, lengths)
    if j + 1 < len(grid[i]) and grid[i][j] - grid[i][j+1] >= -1:
        calc(i, j + 1, curr + 1, grid, lengths)

calc(start[0], start[1], 0, grid, lengths)
print(lengths[end[0]][end[1]])

mn = 440
for i, l in enumerate(grid):
    for j, e in enumerate(l):
        lengths = [[999 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        if e == 0:
            calc(i, j, 0, grid, lengths)
            res = lengths[end[0]][end[1]]
            mn = min(mn, res)
print(mn)
