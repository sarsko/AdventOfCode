print(max(map(sum, [map(int, l.split()) for l in open("input.txt").read().split("\n\n")])))
print(sum(sorted(map(sum, [map(int, l.split()) for l in open("input.txt").read().split("\n\n")]))[-3:]))
