start = 138307
end = 654504
# PART 1
cntr = 0
for i in range(start, end):
    valid = False
    prev = 0
    for e in str(i):
        if int(e) == prev:
            valid = True
            break
        prev = int(e)
    prev = 0
    for e in str(i):
        if int(e) < prev:
            valid = False
            break
        prev = int(e)
    if valid:
        cntr+=1
print(cntr)

# PART 2
cntr = 0
for i in range(start, end):
    valid = False
    prev = 0
    group = ""
    for e in str(i):
        if int(e) == prev:
            group += e
        else:
            if len(group) == 2:
                valid = True
                break
            group = e
        prev = int(e)
    if len(group) == 2:
        valid = True
    prev = 0
    for e in str(i):
        if int(e) < prev:
            valid = False
            break
        prev = int(e)
    if valid:
        cntr+=1
print(cntr)
