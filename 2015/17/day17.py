inp = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

counts = [0 for _ in range(len(inp))]

def is_possible(idx, curr, numconts):
    if curr == 150:
        counts[numconts] += 1
        return 1
    if idx >= len(inp) or curr > 150:
        return 0

    return is_possible(idx+1, curr, numconts) + is_possible(idx+1, curr + inp[idx], numconts+1)

print(is_possible(0, 0, 0))
print(counts)
