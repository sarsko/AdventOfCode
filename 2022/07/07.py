from collections import defaultdict

inp = map(lambda x: x.split(), open("input.txt").read().strip().split("\n"))

i = 0
currdir = []
szes = defaultdict(int)

for i, cmd in enumerate(inp):
    if cmd[1] == "cd":
        if cmd[2] == "..":
            currdir.pop()
        else:
            currdir.append(cmd[2])
    elif cmd[1] != "ls" and cmd[0] != "dir":
        sz = int(cmd[0])
        for j in range(len(currdir)):
            szes[str(currdir[:j+1])] += sz


print(sum([v for v in szes.values() if v <= 100000]))

have = 70000000 - szes[str(["/"])]
print(min([v for v in szes.values() if v + have >= 30000000]))
