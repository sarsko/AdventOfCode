rules = {}
ru, molec = open("input.txt").read().strip().split("\n\n")
#ru, molec = open("example.txt").read().strip().split("\n\n")
for r in ru.split("\n"):
    f, _, t = r.split()
    if f in rules:
        rules[f].append(t)
    else:
        rules[f] = [t]

seen = set()

for i in range(len(molec)):
    for k, v in rules.items():
        if molec[i:].startswith(k):
            for e in v:
                new = molec[:i] + e + molec[i + len(k):]
                seen.add(new)

print(len(seen))

molec = molec.replace("Rn", "")
molec = molec.replace("Ar", "")
molec = molec.replace("Al", "Z")
molec = molec.replace("Ca", "Z")
molec = molec.replace("Mg", "Z")
molec = molec.replace("Si", "Z")
molec = molec.replace("Th", "Z")
molec = molec.replace("Ti", "Z")
print(len(molec) - molec.count("Y") * 2 - 1)
