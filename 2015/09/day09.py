from itertools import permutations

d = {}
cities = set()
for line in open("input.txt").read().strip().split("\n"):
    f, _, t, _, r= line.split(" ")
    d[(f, t)] = int(r)
    d[(t, f)] = int(r)
    cities.add(f)
    cities.add(t)

min_dist = 99999999
longest = 0
for e in permutations(cities):
    dist = 0
    for i in range(len(e)-1):
        dist += d[(e[i], e[i+1])]
    min_dist = min(min_dist, dist)
    longest = max(longest, dist)
print(min_dist)
print(longest)
