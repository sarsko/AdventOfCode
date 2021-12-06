import copy
from collections import defaultdict
def solve(totals, tree, node):
    seen = defaultdict(int)
    wtokey = {}
    for v in tree[node]:
        seen[totals[v]] += 1
        wtokey[totals[v]] = v
    print(seen)
    if len(seen) == 1:
        print(node, totals[node])
    for k, v in seen.items():
        if v == 1:
            return solve(totals, tree, wtokey[k])
def both():
    f = open("input.txt", "r").readlines()
    tree = {}
    weights = {}
    for e in f:
        curr = e.split()
        tree[curr[0]] = set()
        weight = int(curr[1][1:-1])
        weights[curr[0]] = weight
    for e in f:
        curr = e.split()
        if len(curr) > 2:
            for o in curr[3:]:
                o = o.strip(",")
                tree[curr[0]].add(o)
    tree_orig = copy.deepcopy(tree)
    stab = False
    while not stab:
        stab = True
        for k, v in tree.items():
            curr_v = list(v)
            for e in curr_v:
                if e in tree:
                    for o in tree[e]:
                        if o not in tree[k]:
                            tree[k].add(o)
                            stab = False
    mapover = list(tree.values())
    lengs = list(map(len, mapover))
    for k, v in tree.items():
        if len(v) == max(lengs):
            root = k
            print(k)
    totals = {}
    for k, v in tree.items():
        w = weights[k]
        if len(v) > 0:
            for e in v:
                if e in weights:
                    w += weights[e]
        totals[k] = w
    solve(totals, tree_orig, root)
both()
