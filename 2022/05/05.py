def boxes_init():
    return [
        [],
        list("DTWFJSHN"),
        list("HRPQTNBG"),
        list("LQV"),
        list("NBSWRQ"),
        list("NDFTVMB"),
        list("MDBVHTR"),
        list("DBQJ"),
        list("DNJVRZHQ"),
        list("BNHMS"),
    ]

def parse_command(command):
    _, num, _, start, _, end = command.split()
    return (int(num), int(start), int(end))

_, commands = open("input.txt").read().split("\n\n")

# Part 1
boxes = boxes_init()

for line in commands.strip().split("\n"):
    num, start, end = parse_command(line)
    for _ in range(num):
        if boxes[start]:
            boxes[end].append(boxes[start].pop())
        else:
            break

print("".join(bx[-1] for bx in boxes if bx))


# Part 2
boxes = boxes_init()

for line in commands.strip().split("\n"):
    num, start, end = parse_command(line)
    tmp = []
    for _ in range(num):
        if boxes[start]:
            tmp.append(boxes[start].pop())
        else:
            break
    while tmp:
        boxes[end].append(tmp.pop())

print("".join(bx[-1] for bx in boxes if bx))
