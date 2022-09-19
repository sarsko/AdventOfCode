caps = []
durs = []
flavs = []
texts = []
cals = []
for l in open("input.txt").read().strip().split("\n"):
    l = l.replace(",", "")
    name, capacity, cap, durability, dur, flavor, flav, texture, text, calories, cal = l.split()
    caps.append(int(cap))
    durs.append(int(dur))
    flavs.append(int(flav))
    texts.append(int(text))
    cals.append(int(cal))

bst = 0
bst_cal = 0
for i in range(100):
    for j in range(100-i):
        for k in range(100-j-i):
            rst = 100-i-j-k
            cap = caps[0] * i + caps[1] * j + caps[2] * k + caps[3] * rst
            dur = durs[0] * i + durs[1] * j + durs[2] * k + durs[3] * rst
            flav = flavs[0] * i + flavs[1] * j + flavs[2] * k + flavs[3] * rst
            text = texts[0] * i + texts[1] * j + texts[2] * k + texts[3] * rst
            cal = cals[0] * i + cals[1] * j + cals[2] * k + cals[3] * rst
            if cap <= 0 or dur <= 0 or flav <= 0:
                continue
            curr = cap * dur * flav * text
            if cal == 500:
                bst_cal = max(bst_cal, curr)
            bst = max(bst, curr)
print(bst)
print(bst_cal)
