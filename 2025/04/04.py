a = [list(l) for l in open("input.txt").read().split()]
a2 = [row[:] for row in a]
prev = 0
p2 = 0

def get_cnt(grid):
    p1 = 0
    m, n = len(grid), len(grid[0])
    
    def is_valid(i, j):
        return 0 <= i < m and 0 <= j < n

    def neighbors(i, j):
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]:
            ni, nj = i+di, j+dj
            if is_valid(ni, nj):
                yield ni, nj

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                cnt = 0
                for xi, xj in neighbors(i, j):
                    if grid[xi][xj] == "@":
                        cnt += 1
                if cnt < 4:
                    a2[i][j] = "#"
                    p1 += 1
    return p1

while True:
    p1 = get_cnt(a)
    if p2 == 0:
        print(p1)
    if p1 == 0:
        break
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a2[i][j] == "#":
                a[i][j] = "."
    p2 += p1
print(p2)
