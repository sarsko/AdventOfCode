cost = 0

weps = [(4, 8), (5, 10), (6, 25), (7, 40), (8, 74)]
armor = [0, 13, 31, 53, 75, 102]
rings = [(0, 0, 0), (25, 1, 0), (20, 0, 1), (45, 1, 1), (50, 2, 0), (40, 0, 2),
         (100, 3, 0), (180, 3, 3), (140, 3, 2), (130, 2, 3), (80, 0, 3), (105, 1, 3),
         (65, 1, 2)]

def fight(att, defence):
    player = 100
    boss = 103
    bdmg = 9
    barmor = 2
    while player > 0 or boss > 0:
        boss -= att
        boss += barmor
        if boss <= 0:
            return True
        player -= bdmg
        player += defence
        if player <= 0:
            return False
mincost = 99999999
maxcost = 0
for w in weps:
    for i, a in enumerate(armor):
        for c, dmg, arm in rings:
            cost = w[1] + a + c
            if fight(w[0] + dmg, i + arm):
                mincost = min(mincost, cost)
            else:
                maxcost = max(maxcost, cost)
print(mincost)
print(maxcost)
