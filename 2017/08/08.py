from collections import defaultdict
regs = defaultdict(int)
seen = set()
for line in open("input.txt", "r").readlines():
    reg, ins, val, _, ot, cmp, oval = line.split()
    if eval(str(regs[ot]) + cmp + oval):
        if ins == "dec":
            regs[reg] -= int(val)
        else:
            regs[reg] += int(val)
        seen.add(regs[reg])
print(max(regs.values()))
print(max(seen))
