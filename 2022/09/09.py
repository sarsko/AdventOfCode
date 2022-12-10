def sign(x):
    if x == 0:
        return 0
    return [-1, 1][x > 0]

rope = [[0,0] for _ in range(10)]
part2 = set()
part1 = set()

for line in open("input.txt").read().strip().split("\n"):
    l, r = line.split()
    inc = [1,-1][l == "L" or l == "D"]
    i = [0,1][l == "R" or l == "L"]
    for _ in range(int(r)):
        rope[0][i] += inc
        for j in range(1, 10):
            dist = abs(rope[j-1][0] - rope[j][0]) + abs(rope[j-1][1] - rope[j][1])

            if (rope[j-1][0] == rope[j][0] or rope[j-1][1] == rope[j][1]) and dist > 1 or dist > 2:
                rope[j][1] += sign(rope[j-1][1] - rope[j][1])
                rope[j][0] += sign(rope[j-1][0] - rope[j][0])

        part1.add(tuple(rope[1]))
        part2.add(tuple(rope[-1]))

print(len(part1))
print(len(part2))
