removed = 0
for l in open("input.txt").read().strip().split("\n"):
    removed += 2
    removed += l.count("\\\\")
    l = l.replace("\\\\", "")
    removed += l.count("\\x") * 3
    l = l.replace("\\x", "")
    removed += l.count("\\")
print(removed)

added = 0
for l in open("input.txt").read().strip().split("\n"):
    added += 4
    l = l[1:-1]
    added += l.count("\\")
    added += l.count("\"")
print(added)
