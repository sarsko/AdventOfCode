i = 0
regs = {"a": 1, "b": 0}

insts = open("input.txt").read().strip().replace(",", "").split("\n")
while i < len(insts):
    inst = insts[i].split()
    com = inst[0]
    if com == "jio":
        reg = inst[1]
        off = inst[2]
        if regs[reg] == 1:
            i = i + int(off)
        else:
            i += 1
    elif com == "jie":
        reg = inst[1]
        off = inst[2]
        if regs[reg] % 2 == 0:
            i = i + int(off)
        else:
            i += 1
    elif com == "jmp":
        off = inst[1]
        i = i + int(off)
    else:
        reg = inst[1]
        if com == "hlf":
            regs[reg] = regs[reg] // 2
        elif com == "tpl":
            regs[reg] *= 3
        elif com == "inc":
            regs[reg] += 1
        i += 1

print(regs)
