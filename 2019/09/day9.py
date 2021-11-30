inp = [e.zfill(5) for e in open("input.txt", "r").read().strip().split(",")]
for _ in range(1000000):
    inp.append("00000")

i = 0
relativebase = 0
while True:
    op = inp[i]
    tenthousand = int(op[0])
    thousand = int(op[1])
    hundred = int(op[2])
    op = int(op[3:])

    if op == 99:
        break

    firstarg = int(inp[i+1])
    if hundred == 2:
        firstarg += relativebase
    if op == 3 or op == 4:
        if op == 3:
            stored = input().zfill(5)
            inp[firstarg] = str(stored)
        elif op == 4:
            print(inp[firstarg])
        i += 2
    else:
        if hundred == 0 or hundred == 2:
            firstarg = int(inp[firstarg])
        secarg = int(inp[i+2])
        if thousand == 2:
            secarg += relativebase
        if thousand == 0 or thousand == 2:
            secarg = int(inp[secarg])
        if op == 1 or op == 2 or op == 7 or op == 8:
            thirdarg = int(inp[i+3])
            if tenthousand == 2:
                thirdarg += relativebase
            if op == 1:
                inp[thirdarg] = str(firstarg + secarg)
            elif op == 2:
                inp[thirdarg] = str(firstarg * secarg)
            else:
                if op == 7:
                    test = firstarg < secarg
                elif op == 8:
                    test = firstarg == secarg
                if test:
                    inp[thirdarg] = "1".zfill(5)
                else:
                    inp[thirdarg] = "0".zfill(5)
            i += 4
        elif op == 5:
            i += 3
            if firstarg != 0:
                i = secarg
        elif op == 6:
            i += 3
            if firstarg == 0:
                i = secarg
        elif op == 9:
            relativebase += firstarg
            i += 2
        else:
            print("seems wrong")
            print(op)
            break
