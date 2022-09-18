arr = [[0 for _ in range(1000)] for _ in range(1000)]
for l in open("input.txt").read().strip().split("\n"):
    c = l.split()
    ex, ey = map(int, c[-1].split(","))
    if c[0] == "turn":
        sx, sy = map(int, c[2].split(","))
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                arr[i][j] = int(c[1] == "on")
    else: # Toggle
        sx, sy = map(int, c[1].split(","))
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                arr[i][j] = int(arr[i][j] == 0)
print(sum(sum(arr,[])))

arr = [[0 for _ in range(1000)] for _ in range(1000)]
for l in open("input.txt").read().strip().split("\n"):
    c = l.split()
    ex, ey = map(int, c[-1].split(","))
    if c[0] == "turn":
        sx, sy = map(int, c[2].split(","))
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                if c[1] == "on":
                    arr[i][j] += 1
                else:
                    arr[i][j] = max(0, arr[i][j] - 1)
    else: # Toggle
        sx, sy = map(int, c[1].split(","))
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                arr[i][j] += 2
print(sum(sum(arr,[])))
