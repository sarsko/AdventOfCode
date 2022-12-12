from operator import mod, floordiv, add, mul, pow

def do_monkey(monkeys, inspected, i, iftrue, iffalse, op, rhs, mod, change_op, change_param):
    for e in monkeys[i]:
        inspected[i] += 1
        worry = op(change_op(e, change_param), rhs)
        if worry % mod == 0:
            monkeys[iftrue].append(worry)
        else:
            monkeys[iffalse].append(worry)
    monkeys[i] = []

def solve(num_iterations, op, rhs):
    monkeys = [
            [99, 67, 92, 61, 83, 64, 98],
            [78, 74, 88, 89, 50],
            [98, 91],
            [59, 72, 94, 91, 79, 88, 94, 51],
            [95, 72, 78],
            [76],
            [69, 60, 53, 89, 71, 88],
            [72, 54, 63, 80],
    ]
    inspected = [0 for _ in range(8)]

    for _ in range(num_iterations):
        do_monkey(monkeys, inspected, 0, 4, 2, op, rhs, 3, mul, 17)
        do_monkey(monkeys, inspected, 1, 3, 5, op, rhs, 5, mul, 11)
        do_monkey(monkeys, inspected, 2, 6, 4, op, rhs, 2, add, 4)
        do_monkey(monkeys, inspected, 3, 0, 5, op, rhs, 13, pow, 2)
        do_monkey(monkeys, inspected, 4, 7, 6, op, rhs, 11, add, 7)
        do_monkey(monkeys, inspected, 5, 0, 2, op, rhs, 17, add, 8)
        do_monkey(monkeys, inspected, 6, 7, 1, op, rhs, 19, add, 5)
        do_monkey(monkeys, inspected, 7, 1, 3, op, rhs, 7, add, 3)

    inspected.sort()
    return inspected[-1] * inspected[-2]

print(solve(20, floordiv, 3))
print(solve(10000, mod, 7 * 19 * 17 * 11 * 13 * 2 * 5 * 3))
