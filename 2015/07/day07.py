
def parse(l):
    if l[0] == "NOT":
        return ~int(l[1])
    le = int(l[0])
    ri = int(l[2])
    c = l[1]
    if c == "AND":
        return le & ri
    elif c == "OR":
        return le | ri
    elif c == "LSHIFT":
        return le << ri
    elif c == "RSHIFT":
        return le >> ri

g = {}
for l in open("input.txt").read().strip().split("\n"):
    fr, to = l.split("-> ")
    g[to] = fr.split()
acts = {}
done = False
while not done:
    done = True
    for k, v in g.items():
        if type(v) != list:
            continue
        if len(v) == 1 and v[0].isnumeric():
            if k not in acts:
                acts[k] = int(v[0])
                done = False
        else:
            new = []
            varcnt = 0
            for e in v:
                if e in acts:
                    new.append(acts[e])
                else:
                    if type(e) != int and e.islower():
                        varcnt += 1
                    new.append(e)
            if varcnt > 0:
                g[k] = new
            else:
                if len(new) == 1:
                    res = new[0]
                else:
                    res = parse(new)
                g[k] = res
                acts[k] = res
                done = False
print(acts["a"])

g = {}
for l in open("input.txt").read().strip().split("\n"):
    fr, to = l.split("-> ")
    g[to] = fr.split()

acts = {}
acts["b"] = 3176
done = False
while not done:
    done = True
    for k, v in g.items():
        if type(v) != list:
            continue
        if len(v) == 1 and v[0].isnumeric():
            if k not in acts:
                acts[k] = int(v[0])
                done = False
        else:
            new = []
            varcnt = 0
            for e in v:
                if e in acts:
                    new.append(acts[e])
                else:
                    if type(e) != int and e.islower():
                        varcnt += 1
                    new.append(e)
            if varcnt > 0:
                g[k] = new
            else:
                if len(new) == 1:
                    res = new[0]
                else:
                    res = parse(new)
                g[k] = res
                acts[k] = res
                done = False
print(acts["a"])
