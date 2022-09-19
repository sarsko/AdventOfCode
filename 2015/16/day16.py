for l in open("input.txt").read().strip().split("\n"):
    l = l.replace(",", "").replace(":", "")
    if "akitas" in l and not "akitas 0" in l:
        continue
    if "vizslas" in l and not "vizslas 0" in l:
        continue
    if "children" in l and not "children 3" in l:
        continue
    if "samoyeds" in l and not "samoyeds 2" in l:
        continue
    if "cars" in l and not "cars 2" in l:
        continue
    if "perfumes" in l and not "perfumes 1" in l:
        continue
    """
    if "cats" in l and not "cats 3" in l:
        continue
    if "trees" in l and not "trees 3" in l:
        continue
    if "pomeranians" in l and not "pomeranians 3" in l:
        continue
    if "goldfish" in l and not "goldfish 5" in l:
        continue
    """
    print(l)
