from itertools import permutations

people = set()
d = {}

for l in open("input.txt").read().strip().split("\n"):
    n, _, gain, num, _, _, _, _, _,  _, o = l.split()
    o = o[:-1]
    people.add(n)
    people.add(o)
    num = int(num)
    if gain == "lose":
        num = -num
    d[(n, o)] = num

def calc_best():
    best = 0
    for perm in permutations(people):
        curr = 0
        for i, e in enumerate(perm):
            curr += d[(perm[i-1], e)]
            curr += d[(e, perm[i-1])]
        if curr > best:
            best = curr
    return best

print(calc_best())

for e in people:
    d[("self", e)] = 0
    d[(e, "self")] = 0
people.add("self")

print(calc_best())

