import re
from json import loads

f = open("input.txt").read()
res = re.findall("[-+]?[\d]+", f)
print(sum(map(int, res)))

def parse(val):
    if type(val) == int:
        return val
    elif type(val) == list:
        return sum([parse(e) for e in val])
    elif type(val) != dict or "red" in val.values():
        return 0
    return parse(list(val.values()))

l = loads(f)
print(parse(l))
