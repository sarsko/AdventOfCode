f = open("input.txt", "r").read()
l = list(map(int, f.split(",")))

min = 99999999999
min2 = 99999999999
for i in range(1000):
    cost = 0
    cost2 = 0
    for e in l:
        a = abs(i - e)
        cost += a
        cost2 += a * (a + 1) // 2
    if cost < min:
        min = cost
    if cost2 < min2:
        min2 = cost2
print(min)
print(min2)
