# tf = [int(x.strip().split()[-1]) for x in open('2015/inputs/input-00.txt').readlines()]
f = [int(x.strip().split()[-1])
     for x in open('2015/inputs/input-21.txt').readlines()]


def equip(item, dmg_p, arm_p, gold_spent):
    return dmg_p + item[1], arm_p + item[2], gold_spent + item[0]


def part1_and_2(f, result='win'):
    # (cost, damage, armor)
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armor = [(0, 0, 0), (13, 0, 1), (31, 0, 2),
             (53, 0, 3), (75, 0, 4), (102, 0, 5)]
    rings = [
        (0, 0, 0),
        (25, 1, 0), (50, 2, 0), (100, 3, 0),
        (20, 0, 1), (40, 0, 2), (80, 0, 3)
    ]
    min_gold_spent = float('inf')
    max_gold_spent = 0
    for w in weapons:
        for a in armor:
            for r1 in rings:
                for r2 in rings:
                    if r1 == r2:
                        continue

                    hp_b, dmg_b, arm_b = f
                    hp_p, dmg_p, arm_p = 100, 0, 0
                    gold_spent = 0
                    for el in [w, a, r1, r2]:
                        dmg_p, arm_p, gold_spent = equip(el, dmg_p, arm_p, gold_spent)
                    # print(f"\nGold spent: {gold_spent}\nStats: dmg={dmg_p}, arm={arm_p}\n")
                    while True:
                        # print(f"player: {hp_p}, boss: {hp_b}")
                        hp_b -= max(dmg_p - arm_b, 1)
                        if hp_b <= 0:
                            min_gold_spent = min(min_gold_spent, gold_spent)
                            break
                        hp_p -= max(dmg_b - arm_p, 1)
                        if hp_p <= 0:
                            max_gold_spent = max(max_gold_spent, gold_spent)
                            break
                    # print(f"player: {hp_p}, boss: {hp_b}")
    return min_gold_spent, max_gold_spent


# uncomment code to have some RPG fun!
print(f"part 1:\n{ part1_and_2(f)[0] }")
print(f"part 2:\n{ part1_and_2(f)[1] }")
