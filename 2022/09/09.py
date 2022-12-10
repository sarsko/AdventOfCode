def sign(x):
    if x < 0:
        return -1
    return x > 0

rope = [[0,0] for _ in range(10)]
part2 = set()
part1 = set()

for line in open("input.txt").read().strip().split("\n"):
    l, r = line.split()
    inc = [1,-1][l in {"L", "D"}]
    i = l in {"R", "L"}
    for _ in range(int(r)):
        rope[0][i] += inc
        for j in range(1, 10):
            dist = abs(rope[j-1][0] - rope[j][0]) + abs(rope[j-1][1] - rope[j][1])

            if dist > 2 or 1 in map(int.__eq__, rope[j], rope[j-1]) and dist > 1:

                rope[j][1] += sign(rope[j-1][1] - rope[j][1])
                rope[j][0] += sign(rope[j-1][0] - rope[j][0])

        part1.add(tuple(rope[1]))
        part2.add(tuple(rope[-1]))

print(len(part1))
print(len(part2))
