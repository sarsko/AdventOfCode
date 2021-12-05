def part1():
    f = open("input.txt", "r")
    l = list(map(int, f))
    i = 0
    steps = 0
    while True:
        print(i)
        try:
            l[i] += 1
            i += l[i] -1
        except:
            break
        steps += 1
    print(steps)

def part2():
    f = open("input.txt", "r")
    l = list(map(int, f))
    i = 0
    steps = 0
    while True:
        try:
            tmp = l[i]
            if l[i] >= 3:
                l[i] -= 1
            else:
                l[i] += 1
            i += tmp
        except:
            break
        steps += 1
    print(steps)

part1()
part2()
