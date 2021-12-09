f = [line.split() for line in open("input.txt", "r").readlines()]
for i, l in enumerate(f):
    for j, e in enumerate(l):
        if e.isnumeric():
            f[i][j] = "Num("+e+")"
        elif e == "*":
            f[i][j] = "+"
        elif e == "+":
            f[i][j] = "*"
class Num:
    def __init__(self, n):
        self.n = n
    def __add__(self, other):
        return Num(self.n * other.n)
    def __mul__(self, other):
        return Num(self.n + other.n)
    def __str__(self):
        return str(self.n)
print(sum([eval("".join(l)).n for l in f]))

