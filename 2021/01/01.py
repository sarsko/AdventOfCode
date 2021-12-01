f = open("input.txt", "r")
l = list(map(int, f))

# Part 1
incr = -1
prev = 0
for e in l:
    if e > prev:
        incr += 1
    prev = e
print(incr)

# Part 2
incr = -1
prev = 0
for i, _ in enumerate(l):
    try:
        curr = l[i] + l[i+1] + l[i+2]
    except:
        print(incr)
        break
    if curr > prev:
        incr += 1
    prev = curr

