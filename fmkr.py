# initialize with `py fmkr.py YEAR DAY`
# DAY is optional

import sys
import os


def init():
    if len(sys.argv) < 2:
        print('Please, specify a year as an argument.\nYou can also add a third argument to specify a day.')
        return
    
    year = str(sys.argv[1])

    path = os.getcwd()
    year_path = path + '\\' + year

    if year not in os.listdir(path):
        os.mkdir(year_path)

    if 'inputs' not in os.listdir(year_path):
        os.mkdir(year_path + '\inputs')

    if 'input-00.txt' not in os.listdir(year_path + '\inputs'):
        open(year_path + '\inputs\input-00.txt', 'w+').close()
        
    if len(sys.argv) == 2:
        day = max([int(name.strip('day-').strip('.py')) for name in os.listdir(os.getcwd() + '\\' + year) if 'day-' in name] + [0]) + 1
    else:
        day = str(sys.argv[2])
    
    day_str = [str(day) if len(str(day)) > 1 else '0' + str(day)][0]

    f = open(year_path + '\day-' + day_str + '.py', 'w+')
    p1_str = 'f"part 1:\\n{ part1(f) }"'
    p2_str = 'f"part 2:\\n{ part2(f) }"'
    f.write(f"tf = [x.strip() for x in open('{ year }/inputs/input-00.txt').readlines()]\nf = [x.strip() for x in open('{ year }/inputs/input-{ day_str }.txt').readlines()]\n\n\ndef part1(f): return f\n\n\ndef part2(f): return None\n\n\nprint({ p1_str })\nprint({ p2_str })")
    f.close()
    open(year_path + '\inputs\input-' + day_str + '.txt', 'w+').close()

init()
