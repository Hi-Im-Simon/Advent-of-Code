f = [int(x.strip().split()[-1]) for x in open('2015/inputs/input-22.txt').readlines()]


def check_mana_used(mana_used):
    global min_mana_used
    min_mana_used = min(min_mana_used, mana_used)

def rec(hp_p, mana_p, hp_b, mana_used, active_effects, turn='player'):
    global dmg_b_0, arm_p_0
    
    # for RPG
    t_m, t_hpb = mana_p, hp_b
    
    # I HATE THIS, BUT IT HAS TO BE DONE FOR SOME REASON
    active_effects = active_effects.copy()
    # apply currently active effects
    if active_effects['shield'] > 0:
        dmg_b = max(dmg_b_0 - arm_p_0 - 7, 1)
    else:
        dmg_b = dmg_b_0 - arm_p_0
    if active_effects['poison'] > 0:
        hp_b -= 3
    if active_effects['recharge'] > 0:
        mana_p += 101
    
    # active effect wear off
    for eff in ['shield', 'poison', 'recharge']:
        if active_effects[eff] > 0:
            active_effects[eff] -= 1
    
    # check if boss dies from poison
    if hp_b <= 0:
        check_mana_used(mana_used)
        return
    
    # if player's turn
    if turn == 'player':
        # cast a spell and attack as a boss
        if mana_p >= 53:
            if hp_b - 4 <= 0:
                check_mana_used(mana_used)
                return
            # print(f'\n-- {turn} turn --')
            # print(f'Player: hp={hp_p}, mana={t_m}')
            # print(f'Boss: hp={t_hpb}')
            # print(f'{active_effects}\nCast: Magic Missile')
            rec(hp_p, mana_p-53, hp_b-4, mana_used+53, active_effects, 'boss')
        if mana_p >= 73:
            if hp_b - 2 <= 0:
                check_mana_used(mana_used)
                return
            # print(f'\n-- {turn} turn --')
            # print(f'Player: hp={hp_p}, mana={t_m}')
            # print(f'Boss: hp={t_hpb}')
            # print(f'{active_effects}\nCast: Drain')
            rec(hp_p+2, mana_p-73, hp_b-2, mana_used+73, active_effects, 'boss')
        if mana_p >= 113 and not active_effects['shield']:
            a_e = active_effects.copy()
            a_e['shield'] = 6
            # print(f'\n-- {turn} turn --')
            # print(f'Player: hp={hp_p}, mana={t_m}')
            # print(f'Boss: hp={t_hpb}')
            # print(f'{active_effects}\nCast: Shield')
            rec(hp_p, mana_p-113, hp_b, mana_used+113, a_e, 'boss')
        if mana_p >= 173 and not active_effects['poison']:
            a_e = active_effects.copy()
            a_e['poison'] = 6
            # print(f'\n-- {turn} turn --')
            # print(f'Player: hp={hp_p}, mana={t_m}')
            # print(f'Boss: hp={t_hpb}')
            # print(f'{active_effects}\nCast: Poison')
            rec(hp_p, mana_p-173, hp_b, mana_used+173, a_e, 'boss')
        if mana_p >= 229 and not active_effects['recharge']:
            a_e = active_effects.copy()
            a_e['recharge'] = 5
            # print(f'\n-- {turn} turn --')
            # print(f'Player: hp={hp_p}, mana={t_m}')
            # print(f'Boss: hp={t_hpb}')
            # print(f'{active_effects}\nCast: Recharge')
            rec(hp_p, mana_p-229, hp_b, mana_used+229, a_e, 'boss')
        else:
            return
        
    # if boss' turn
    elif turn == 'boss':
        if hp_p - dmg_b <= 0:
            return
        # print(f'\n-- {turn} turn --')
        # print(f'Player: hp={hp_p}, mana={t_m}')
        # print(f'Boss: hp={t_hpb}')
        # print(f'{active_effects}')
        rec(hp_p-dmg_b, mana_p, hp_b, mana_used, active_effects, 'player')


def part1():
    active_effects = {
        'shield': 0,
        'poison': 0,
        'recharge': 0
    }
    global hp_p_0, mana_p_0, hp_b_0
    rec(hp_p_0, mana_p_0, hp_b_0, 0, active_effects)
    global min_mana_used
    return min_mana_used


def part2(f): return None


min_mana_used = float('inf')
hp_b_0, dmg_b_0 = f[0], f[1]
hp_p_0, arm_p_0, mana_p_0 = 50, 0, 500

print(f"part 1:\n{ part1() }")
print(f"part 2:\n{ part2(f) }")
