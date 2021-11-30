# PART 1
f = open("input.txt", "r")
rtot = 0
for line in f.readlines():
    rtot += int(line) // 3 - 2
print(rtot)

# PART 2
f = open("input.txt", "r")
rtot = 0
for line in f.readlines():
    tmp = 0
    inc = int(line) // 3 - 2
    while inc > 0:
        tmp+=inc
        inc = inc // 3 - 2
    rtot += tmp
print(rtot)
