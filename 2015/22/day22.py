bhp = 71
bdmg = 10
php = 50
mana = 500
manaspent = 0
poison = 0
recharge = 0
shield = 0
totmana = 0

# Value: Drain: 36.5, poison: 9.6, missile: 26.5
# Less than 2166 total mana spent
"""
while True:
    if poison:
        bhp -= 3
        poison -= 1
    if recharge:
        mana += 101
        recharge -= 1
    if shield:
        shield -= 1
    if bhp <= 0:
        print("You win! Total mana spent:", totmana)
        break
    print("The boss currently has", bhp, "health")
    print("You have", php, "health, and", mana, "mana")
    print("Poison:", poison, "recharge:", recharge, "shield:", shield)
    action = int(input())
    if action == 1:
        bhp -= 4
        mana -= 53
        totmana += 53
    elif action == 2:
        bhp -= 2
        php += 2
        mana -= 73
        totmana += 73
    elif action == 3:
        shield = 6
        mana -= 113
        totmana += 113
    elif action == 4:
        poison = 6
        mana -= 173
        totmana += 173
    elif action == 5:
        recharge = 5
        mana -= 229
        totmana += 229
    php -= bdmg
    if poison:
        bhp -= 3
        poison -= 1
    if recharge:
        mana += 101
        recharge -= 1
    if bhp <= 0:
        print("You win! Total mana spent:", totmana)
        break
    if shield:
        php += 7
        shield -= 1
    if php <= 0:
        print("You lose!")
        break
"""
mana_cap = 2166
# 1824 and 1937
def fight(bhp, php, mana, poison, recharge, shield, totmana):
    global mana_cap

    # part 2
    php -= 1
    if php <= 0:
        return

    if totmana >= mana_cap:
        return
    if poison:
        bhp -= 3
        poison -= 1
    if recharge:
        mana += 101
        recharge -= 1
    if shield:
        shield -= 1
    if bhp <= 0:
        mana_cap = min(mana_cap, totmana)
        return
    poss_actions = []
    if mana >= 53:
        poss_actions.append(1)
    if mana >= 73:
        poss_actions.append(2)
    if mana >= 113 and not shield:
        poss_actions.append(3)
    if mana >= 113 and not poison:
        poss_actions.append(4)
    if mana >= 113 and not recharge:
        poss_actions.append(5)
    if not poss_actions:
        return
    old_bhp = bhp
    old_mana = mana
    old_totmana = totmana
    old_php = php
    old_shield = shield
    old_recharge = recharge
    old_poison = poison
    for action in poss_actions:
        bhp = old_bhp
        mana = old_mana
        totmana = old_totmana
        php = old_php
        shield = old_shield
        recharge = old_recharge
        poison = old_poison
        if action == 1:
            bhp -= 4
            mana -= 53
            totmana += 53
        elif action == 2:
            bhp -= 2
            php += 2
            mana -= 73
            totmana += 73
        elif action == 3:
            shield = 6
            mana -= 113
            totmana += 113
        elif action == 4:
            poison = 6
            mana -= 173
            totmana += 173
        elif action == 5:
            recharge = 5
            mana -= 229
            totmana += 229
        php -= bdmg
        if poison:
            bhp -= 3
            poison -= 1
        if recharge:
            mana += 101
            recharge -= 1
        if shield:
            php += 7
            shield -= 1
        if bhp <= 0:
            mana_cap = min(mana_cap, totmana)
            return
        if php <= 0:
            return
        fight(bhp, php, mana, poison, recharge, shield, totmana)
fight(bhp, php, 500, 0, 0, 0, 0)
print(mana_cap)
