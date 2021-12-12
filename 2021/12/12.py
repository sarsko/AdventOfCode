from collections import defaultdict
caves = defaultdict(set)
with open("input.txt", "r") as f:
    for k, v in [l.strip().split("-") for l in f]:
        caves[k].add(v)
        caves[v].add(k)

def findPath(visited, node, repeated):
    if node == "start" or (node.islower() and node in visited and repeated):
        return 0
    if node == "end":
        return 1
    return sum(findPath(visited | {node}, nxt, repeated or (node.islower() and node in visited)) for nxt in caves[node])

print(sum(findPath(set(), e, True) for e in caves["start"]))
print(sum(findPath(set(), e, False) for e in caves["start"]))
