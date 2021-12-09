f = open("input.txt", "r")
dep = 0
hor = 0
aim = 0
for line in f:
    c, n = line.split()
    n = int(n)
    if c == "forward":
        hor+=n
        dep+=n*aim
    elif c == "down":
        aim += n
#        dep+=n
    else:
        aim -= n
#        dep-=n

print(hor*dep)
