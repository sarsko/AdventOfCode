inp = 3600000
pres = [0 for _ in range(inp)]
for i in range(1, inp):
    for j in range(i, inp,i):
        pres[j] += i
for i, e in enumerate(pres):
    if e >= inp:
        print(i)
        break

## part 2
pres = [0 for _ in range(inp)]
for i in range(1, inp):
    num = 0
    for j in range(i, inp,i):
        pres[j] += 11 * i
        num += 1
        if num == 50:
            break
for i, e in enumerate(pres):
    if e >= inp * 10:
        print(i)
        break
