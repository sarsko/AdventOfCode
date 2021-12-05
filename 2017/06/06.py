def both():
    f = open("input.txt", "r")
    l = list(map(int, f.read().split()))
    leng = len(l)
    seen = set()

    cnt = 0
    looper = ""
    loop = 0
    while True:
        if str(l) in seen:
            if not looper:
                print(cnt)
                looper = str(l)
            elif looper == str(l):
                print(loop)
                break
        else:
            seen.add(str(l))
        cnt+=1
        mx = max(l)
        i = l.index(mx)
        l[i] = 0
        for _ in range(mx):
            i = (i + 1) % leng
            l[i] += 1
        if looper:
            loop += 1

both()
