from typing import List

def input_as_string(filename:str) -> str:
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str) -> List[str]:
    return input_as_string(filename).split("\n")

l = input_as_lines("input.txt")
cnt = 0
tot = 0
for e in l:
    d = {}
    b, a = e.split("|")
    b = b.split()
    a = a.split()
    for e2 in b:
        le = len(e2)
        s = set(e2)
        if le == 2:
            d[1] = s
        elif le == 3:
            d[7] = s
        elif le == 4:
            d[4] = s
        elif le == 7:
            d[8] = s
    for e2 in b:
        le = len(e2)
        s = set(e2)
        if le == 6:
            if len(d[1] - s) == 1:
                d[6] = s
            elif len(d[4] - s) == 1:
                d[0] = s
            else:
                d[9] = s
        elif le == 5:
            if len(d[7] - s) == 0:
                d[3] = s
            elif len(d[4] - s) == 1:
                d[5] = s
            else:
                d[2] = s
    tmp = ""
    for e in a:
        s = set(e)
        for k, v in d.items():
            if s == v:
                tmp += str(k)
                if k == 1 or k == 4 or k == 7 or k == 8:
                    cnt += 1
    tot += int(tmp)
print(cnt)
print(tot)
