from collections import defaultdict

rules = {}
alpchcnt = defaultdict(int)
start = defaultdict(int)
with open("input.txt", "r") as f:
    inp = f.read().split("\n\n")

template = inp[0]
for j, e in enumerate(template[:-1]):
    start[e + template[j+1]] += 1
    alpchcnt[e] += 1
alpchcnt[template[-1]] += 1

for line in inp[1].strip().split("\n"):
    k, v = line.split(" -> ")
    rules[k] = v

def nextIt(d):
    while True:
        yield d
        new = defaultdict(int)
        for k, v in d.items():
            match = rules[k]
            new[k[0]+match] += v
            new[match+k[1]] += v
            alpchcnt[match] += v
        d = new

des = {10, 40}
for i, e in enumerate(nextIt(start)):
    if i in des:
        print(max(alpchcnt.items(), key=lambda x:x[1])[1] - min(alpchcnt.items(), key=lambda x:x[1])[1])
        des.remove(i)
    if not des:
        break

