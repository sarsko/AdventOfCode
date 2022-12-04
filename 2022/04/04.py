part1 = 0
part2 = 0
for line in open("input.txt"):
    l, r = line.strip().split(",")
    ll, lr = map(int, l.split("-"))
    rl, rr = map(int, r.split("-"))
    if (ll <= rl and lr >= rr) or (rl <= ll and rr >= lr):
        part1 += 1
    if max(ll, rl) <= min(lr, rr):
        part2 += 1
print(part1)
print(part2)
