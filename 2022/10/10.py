strength = 0
x = 1
cycle = 1
out_arr = []
curr = []

def potentially_add_new_line(out_arr, curr):
    if cycle % 40 == 0:
        out_arr.append(curr)
        return []
    return curr

def generate_crt_for_curr_pix(curr):
    if x in range(cycle%40 - 2, cycle%40 + 1):
        curr.append("#")
    else:
        curr.append(" ")

for l in open("input.txt").read().strip().split("\n"):
    inst = l.split()

    if inst[0] == "noop":
        cycle_cnt = 1
        incr = 0
    elif inst[0] == "addx":
        cycle_cnt = 2
        incr = int(inst[1])

    for _ in range(cycle_cnt):
        generate_crt_for_curr_pix(curr)
        curr = potentially_add_new_line(out_arr, curr)

        if (cycle - 20) % 40 == 0:
            strength += cycle * x

        cycle += 1

    x += int(incr)

print(strength)

for l in out_arr:
    print("".join(l))

