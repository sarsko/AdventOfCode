pairs = {"(":")", "[":"]", "{":"}", "<":">"}
errorScores = {")":3, "]":57, "}":1197, ">":25137}
autoScores = {"(":1, "[":2, "{":3, "<":4}

tots = []
part1 = 0
for l in open("input.txt", "r").read().split("\n"):
    stack = []
    for c in l:
        if c in pairs.keys():
            stack.append(c)
        else:
            if pairs[stack.pop()] != c:
                part1 += errorScores[c]
                break
    else:
        tot = 0
        for e in stack[::-1]:
            tot *= 5
            tot += autoScores[e]
        tots.append(tot)
print(part1)
tots.sort()
print(tots[len(tots)//2])
