import re

rules = {}

file = open("input.txt", "r").read().split("\n\n")
for e in file[0].split("\n"):
    f, s = e.split(":")
    s = s.replace('"', "")
    if "|" in s:
        s = "(?: " + s + " )"
    rules[f] = s.split()

def expandrule(num, rules):
    new = rules["0"].copy()
    done = False
    while not done:
        done = True
        for i, e in enumerate(new):
            if e.isnumeric():
                done = False
                new[i:i+1] = rules[e].copy()
    new.insert(0, "^")
    new.append("$")
    return new

z = expandrule("0", rules)
needle = re.compile("".join(z))

cnt = 0
for e in file[1].split("\n"):
    if needle.match(e):
        cnt += 1
print(cnt)

rules2 = rules.copy()
rules2["8"] = "(?: 42 )+".split()
rules2["11"] = "(?: (?: (?: 42 ) (?: 31 ) ) | (?: (?: 42 ) {2} (?: 31 ) {2} ) | (?: (?: 42 ) {3} (?: 31 ) {3} ) | (?: (?: 42 ) {4} (?: 31 ) {4} ) )".split()

z = expandrule("0", rules2)
needle = re.compile("".join(z))

cnt = 0
for e in file[1].split("\n"):
    if needle.match(e):
        cnt += 1
print(cnt)

