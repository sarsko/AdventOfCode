# PART 1
inp = open("input.txt", "r").read().strip().split(",")
for i, e in enumerate(inp):
    inp[i] = inp[i].zfill(5)
inp_copy = inp[:]
i = 0
while True:
    op = inp[i]
    op_orig = op
    tenthousand = int(op[0])
    thousand = int(op[1])
    hundred = int(op[2])
    op = int(op[3:])
    if op == 3:
        stored = input()
        stored = stored.zfill(5)
        inp[int(inp[i+1])] = str(stored)
        i += 2
    elif op == 4:
        print(inp[int(inp[i+1])])
        i += 2
    elif op == 99:
        break
    else:
        firstarg = int(inp[i+1])
        if not hundred:
            firstarg = int(inp[firstarg])
        secarg = int(inp[i+2])
        if not thousand:
            secarg = int(inp[secarg])

        if op == 1:
            inp[int(inp[i+3])] = str(firstarg + secarg)
            i += 4
        elif op == 2:
            inp[int(inp[i+3])] = str(firstarg * secarg)
            i += 4
        elif op == 5:
            i += 3
            if firstarg != 0:
                i = secarg
        elif op == 6:
            i += 3
            if firstarg == 0:
                i = secarg
        elif op == 7:
            if firstarg < secarg:
                inp[int(inp[i+3])] = "1".zfill(5)
            else:
                inp[int(inp[i+3])] = "0".zfill(5)
            i += 4
        elif op == 8:
            if firstarg == secarg:
                inp[int(inp[i+3])] = "1".zfill(5)
            else:
                inp[int(inp[i+3])] = "0".zfill(5)
            i += 4
        else:
            print("seems wrong")
            print(op)
            break
