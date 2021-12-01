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
    f.write("tf = open('" + year + "/inputs/input-00.txt').read()\nf = open('" + year + "/inputs/input-" + day_str + ".txt').read()\n\n\n\nprint(f)\n#print('part 1:\\n' + str(ans1))\n#print('part 2:\\n' + str(ans2))")
    f.close()
    open(year_path + '\inputs\input-' + day_str + '.txt', 'w+').close()

init()
