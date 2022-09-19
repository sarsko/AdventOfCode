inp = "1113222113"
for i in range(50):
    prev = ""
    cnt = 0
    new = ""
    for e in inp:
        if e != prev:
            if prev:
                new += str(cnt) + prev
            prev = e
            cnt = 1
        else:
            cnt += 1
    new += str(cnt) + prev
    inp = new
    if i == 39:
        print(len(inp))

print(len(inp))
