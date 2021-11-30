import itertools
import copy
inp = open("input.txt", "r").read().strip().split(",")
for i, e in enumerate(inp):
    inp[i] = inp[i].zfill(5)
inp.append("99")
inp.append("99")
inp_copy = inp[:]
all_perms = list(itertools.permutations([0,1,2,3,4]))
highest = 0
for perm in all_perms:
    output = 0
    for j in perm:
        i = 0
        setonce = False
        inp = inp_copy[:]
        while True:
            op = inp[i]
            op_orig = op
            tenthousand = int(op[0])
            thousand = int(op[1])
            hundred = int(op[2])
            op = int(op[3:])
            if op == 3:
                if not setonce:
                    stored = str(j)
                    setonce = True
                else:
                    stored = str(output)
                stored = stored.zfill(5)
                inp[int(inp[i+1])] = str(stored)
                i += 2
            elif op == 4:
                #print(inp[int(inp[i+1])])
                output = inp[int(inp[i+1])]
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
    if int(output) > highest:
        highest = int(output)
print(highest)

# PART 2
all_perms = list(itertools.permutations([5,6,7,8,9]))
all_perms = [list(perm) for perm in all_perms]
highest = 0
for perm in all_perms:
    inps = [copy.deepcopy(inp_copy),copy.deepcopy(inp_copy),copy.deepcopy(inp_copy),copy.deepcopy(inp_copy),copy.deepcopy(inp_copy)]
    output = 0
    setonce = [0,0,0,0,0]
    instctrs = [0,0,0,0,0]
    while len(perm) > 0:
        for e in perm:
            i = instctrs[e-5]
            while True:
                inp = inps[e-5]
                op = inps[e-5][i]
                op_orig = op
                tenthousand = int(op[0])
                thousand = int(op[1])
                hundred = int(op[2])
                op = int(op[3:])
                if op == 3:
                    if not setonce[e-5]:
                        stored = str(e)
                        setonce[e-5] = True
                    else:
                        stored = str(output)
                    stored = stored.zfill(5)
                    inp[int(inps[e-5][i+1])] = str(stored)
                    i += 2
                elif op == 4:
                    output = inp[int(inp[i+1])]
                    i += 2
                    instctrs[e-5] = i
                    break
                elif op == 99:
                    perm.remove(e)
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
    if int(output) > highest:
        highest = int(output)
print(highest)
