# PART 1
inp = list(map(int, open("input.txt", "r").read().strip().split(",")))
inp_copy = inp[:]
inp[1] = 12
inp[2] = 2
i = 0
while True:
    op = inp[i]
    if op == 1:
        inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
    elif op == 2:
        inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
    elif op == 99:
        break
    i += 4
print(inp[0])

# PART 2
needle = 19690720
for j in range(100):
    for k in range(100):
        inp = inp_copy[:]
        inp[1] = j
        inp[2] = k
        i = 0
        while True:
            op = inp[i]
            if op == 1:
                inp[inp[i+3]] = inp[inp[i+1]] + inp[inp[i+2]]
            elif op == 2:
                inp[inp[i+3]] = inp[inp[i+1]] * inp[inp[i+2]]
            elif op == 99:
                break
            i += 4
        if inp[0] == needle:
             print(100*j+k)
