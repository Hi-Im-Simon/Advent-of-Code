# initialize with `py fmkr.py YEAR DAY`
# DAY is optional

import sys
import os
import aocd
from aocd.models import Puzzle

# customize your imports
DEFAULT_HEADER = """
import numpy as np
"""

# error messages
ARG_ERR = """Error: Invalid arguments.\n\nScript accepts 2 argumets:
- year: int - puzzle year valid for AoC
- day: int (optional) - between 1 and 25(included), if not provided, the next one in chosen year will be taken\n"""

AOC_ERR = """Error: Cannot communicate with AoC API.\n
Could not communicate with AoC API. Try manually extracting the session cookie (aocd.cookies.scrape_session_tokens()).
"""

DAY26_ERR = """Error: Files already exist.\n
Files for the final day in chosen year already exist.
Choose a different year or provide a specific day as another argument if you want to add or overwrite one of the days.
"""

PATH = os.path.dirname(__file__)


def init():
    if len(sys.argv) == 2:
        # if only year was provided
        year = int(sys.argv[1])
        if str(year) in os.listdir(PATH):
            day = max([int(f_name.strip('day-').strip('.py')) for f_name in os.listdir(f'{PATH}/{year}') if 'day-' in f_name]) + 1
            if day > 25:
                exit(DAY26_ERR)
        else:
            day = 1
        
    elif len(sys.argv) == 3:
        # if year and day were provided
        year = int(sys.argv[1])
        day = int(sys.argv[2])
    else:
        exit(ARG_ERR)
        
    if year < 2015 or day not in range(1, 26):
        exit(ARG_ERR)
    
    file_number: str = f'{day:02d}'
    file_name_py: str = f'day-{file_number}.py'
    
     # check if files don't already exist,
    # if they do, ask if they should be overwritten
    if (
        str(year) in os.listdir(PATH) and
        file_name_py in os.listdir(f'{PATH}/{year}')
    ):
        if not (input('This file already exists. Overwrite with base data? (Y/n) ').upper() == 'Y'):
            exit('Script cancelled.')
    
    # remove sys args to avoid aocd error
    del sys.argv[1:]
    
    # try scraping AoC session cookie if it doesnt exist yet
    try:
        aocd.cookies.scrape_session_tokens()
    except Exception:
        exit(AOC_ERR)
    
    # check if the year and day are valid with AoC API
    # and get puzzle data if possible
    try:
        puzzle = Puzzle(year=year, day=day)
    except aocd.exceptions.PuzzleLockedError:
        exit(ARG_ERR)
    except Exception as err:
        exit(AOC_ERR)

    # create missing directories and files
    year_path = f'{PATH}/{year}'

    if str(year) not in os.listdir(PATH):
        os.mkdir(year_path)

    if 'inputs' not in os.listdir(year_path):
        os.mkdir(f'{year_path}/inputs')
        
    if 'example-inputs' not in os.listdir(year_path):
        os.mkdir(f'{year_path}/example-inputs')

    # if 'input-00.txt' not in os.listdir(year_path + '\inputs'):
    #     open(year_path + '\inputs\input-00.txt', 'w+').close()
    
    # input file
    with open(f'{year_path}/inputs/input-{file_number}.txt', 'w+') as file:
        file.write(puzzle.input_data)
        
    # example input file
    with open(f'{year_path}/example-inputs/input-{file_number}.txt', 'w+') as file:
        file.write(puzzle.example_data)

    with open(f'{year_path}/{file_name_py}', 'w+') as file:
        file.write(
f"""{DEFAULT_HEADER.strip()}


class Day{ day }:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{{__file__}}/../{{('example-' if use_example_input else '')}}inputs/input-{file_number}.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data = [x.rstrip() for x in file.readlines()]

    def part1(self):
        
    
        return self.data

    def part2(self):
        
    
        return None


d = Day{ day }(use_example_input=False)
print(f"Part 1:\\n{{d.part1()}}")
print(f"Part 2:\\n{{d.part2()}}")
""")
    exit('Script completed successfully.')

if __name__ == '__main__':
    init()
