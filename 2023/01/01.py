m = {
 "one": 1,
 "two": 2,
 "three": 3,
 "four": 4,
 "five": 5,
 "six": 6,
 "seven": 7,
 "eight": 8,
 "nine": 9,
}

rtot = 0
lines = open("input.txt", "r").readlines()
for l in lines:
    c = "".join(filter(str.isdigit, l))
    c += c[-1]
    f = c[0] + c[-1]
    rtot += int(f)
print(rtot)

rtot = 0
for l in lines:
    for k, v in m.items():
        s = list(k)
        s[1] = str(v)
        l = l.replace(k, "".join(s))
    c = "".join(filter(str.isdigit, l))
    c += c[-1]
    f = c[0] + c[-1]
    rtot += int(f)
print(rtot)
