#tf = open('2015/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2015/inputs/input-22.txt').readlines()    # your input data


BASE_HP, BASE_DMG = [int(x.split()[-1]) for x in f]
SPELLS = {'Magic Missile': 53, 'Drain': 73, 'Shield': 113, 'Poison': 173, 'Recharge': 229}
MIN_MANA_USED = float('inf')

class Entity:
    def __init__(self, hp, mana, dmg, armor=0, effects={}, mana_spent=0):
        self.hp = hp
        self.mana = mana
        self.dmg = dmg
        self.armor = armor
        self.effects = effects
        self.mana_spent = mana_spent


def turn(num, Player, Boss, flag):    
    message = f'- Player has {Player.hp} hit points, {Player.armor} armor, {Player.mana} mana\n- Boss has {Boss.hp} hit points'
    
    def apply_effects():
        if 'Shield' in Player.effects:
            Player.armor = 7
        else:
            Player.armor = 0
        if 'Recharge' in Player.effects:
            Player.mana += 101
        if 'Poison' in Boss.effects:
            Boss.hp -= 3
            
        # remove worn off effects
        for Ent in [Player, Boss]:
            for effect in list(Ent.effects):
                Ent.effects[effect] -= 1
                if Ent.effects[effect] == 0:
                    del Ent.effects[effect]
                    if ALERTS: print(f'{effect} wears off.')
                else:
                    if ALERTS: print(f'{effect} timer is now {Ent.effects[effect]}.')
        
    def cast(spell_id):
        if Player.mana < SPELLS[spell_id] or spell_id in Player.effects or spell_id in Boss.effects:
            return 0
        
        if ALERTS: print(f'Player casts {spell_id}.')
        Player.mana -= SPELLS[spell_id]
        Player.mana_spent += SPELLS[spell_id]
        
        match spell_id:
            case 'Magic Missile':
                Boss.hp -= 4
            case 'Drain':
                Boss.hp -= 2
                Player.hp += 2
            case 'Shield':
                Player.effects[spell_id] = 6
            case 'Poison':
                Boss.effects[spell_id] = 6
            case 'Recharge':
                Player.effects[spell_id] = 5
        return 1
        
    def end_fight():
        if Boss.hp <= 0:
            global MIN_MANA_USED
            if WIN_ALERTS: print(f'PLAYER WINS! MANA USED: { Player.mana_spent, MIN_MANA_USED }')
            MIN_MANA_USED = min(MIN_MANA_USED, Player.mana_spent)
            return True
        elif Player.hp <= 0:
            if ALERTS: print('player loses')
            return True
        else:
            return False
    
    def copy(Obj):
            return Entity(Obj.hp, Obj.mana, Obj.dmg, Obj.armor, Obj.effects.copy(), Obj.mana_spent)
    
    if num % 2:
        if flag == 'HARD':
            Player.hp -= 1
            if end_fight(): return
            
        if ALERTS: print(f'\n-- Player turn -- ({ num })\n{ message }')
        apply_effects()
        if end_fight(): return
        
        if Player.mana < min(SPELLS.values()):
            return
        
        for spell in SPELLS:
            if spell in ['Magic Missile', 'Drain'] and Boss.hp > 10 and 'Poison' not in Boss.effects.keys():
                continue
            P_old, B_old = copy(Player), copy(Boss)
            if cast(spell) and not end_fight():
                turn(num + 1, Player, Boss, flag)
            Player, Boss = P_old, B_old
        
    else:
        if ALERTS: print(f'\n-- Boss turn -- ({ num })\n{ message }')
        apply_effects()
        if end_fight(): return
        
        boss_dmg = max(Boss.dmg - Player.armor, 1)
        if ALERTS: print(f'Boss attacks for { boss_dmg } damage!')
        Player.hp -= boss_dmg
        if end_fight(): return
        
        turn(num + 1, Player, Boss, flag)
    

def part1_and_2(flag=''):
    global MIN_MANA_USED
    MIN_MANA_USED = float('inf')
    
    Player = Entity(50, 500, 0)
    Boss = Entity(BASE_HP, 0, BASE_DMG)
    
    turn(1, Player, Boss, flag)
    return MIN_MANA_USED


ALERTS = False
WIN_ALERTS = False
print(f"part 1:\n{ part1_and_2() }")
print(f"part 2:\n{ part1_and_2(flag='HARD') }")
