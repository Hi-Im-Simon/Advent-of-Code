def ch_sort(f):
    passp, p = [''], 0

    for i in range(len(f)):
        if f[i] == '\n':
            p += 1
            passp.append('')
        else: passp[p] += f[i]
    passp = [sorted(passp[i].replace('\n', ' ').split())[::-1] for i in range(len(passp))]

    return passp


def ch1(f):
    passp, ans = ch_sort(f), 0

    for pas in passp:
        if len(pas) > 5:
            if 'byr' not in pas[-1] or 'ecl' not in pas[5] or 'eyr' not in pas[4] or 'hcl' not in pas[3] or 'hgt' not in pas[2] or 'iyr' not in pas[1]  or 'pid' not in pas[0]:
                continue
            else:
                ans += 1
    return ans


def ch2(f):
    passp, ans = ch_sort(f), 0
    av_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for pas in passp:
        if len(pas) > 6:
            if 'byr' not in pas[-1] or 'ecl' not in pas[5] or 'eyr' not in pas[4] or 'hcl' not in pas[3] or 'hgt' not in pas[2] or 'iyr' not in pas[1]  or 'pid' not in pas[0]:
                continue
        else:
            continue

        year = pas[-1].split(':')[1]
        if len(year) != 4 or not 1920 <= int(year) <= 2002: continue

        eyes = pas[5].split(':')[1]
        if eyes not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: continue

        exp_year = pas[4].split(':')[1]
        if len(exp_year) != 4 or not 2020 <= int(exp_year) <= 2030: continue

        hair = pas[3].split(':')[1]
        if len(hair) != 7 or hair[0] != '#' or False in [i in av_chars for i in hair[1:]]: continue

        height = pas[2].split(':')[1]
        if height[-2:] in ['cm', 'in']:
            if height[-2:] == 'cm' and not 150 <= int(height[:-2]) <= 193: continue 
            elif height[-2:] == 'in' and not 59 <= int(height[:-2]) <= 76: continue
        else: continue

        issue_year = pas[1].split(':')[1]
        if len(issue_year) != 4 or not 2010 <= int(issue_year) <= 2020: continue

        pass_id = pas[0].split(':')[1]
        if len(pass_id) != 9 or False in [i in digits for i in pass_id]: continue
        
        ans += 1
    return ans


file = open('c:/Code/Advent of Code/2020/inputs/input-04.txt').readlines()
print(ch1(file))
print(ch2(file))
