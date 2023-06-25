import numpy as np


class Day23:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-23.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[tuple[str|int]] = [tuple([int(y) if y.lstrip('-').isnumeric() else y for y in x.rstrip().split()]) for x in file.readlines()]

    def part1(self, start_a: int):
        data = self.data.copy()
        vals: dict[str, int|None] = {'a': start_a}
        i: int = 0
        
        while i < len(data):
            line: tuple[str|int] = data[i]
            
            if line[0] == 'cpy':
                if type(line[2]) is str:
                    if type(line[1]) is int:
                        vals[line[2]] = line[1]
                    else:
                        if line[1] in vals.keys():
                            vals[line[2]] = vals[line[1]]
            elif line[0] == 'inc':
                if line[1] in vals.keys():
                    vals[line[1]] += 1
            elif line[0] == 'dec':
                if line[1] in vals.keys():
                    vals[line[1]] -= 1
            elif line[0] == 'jnz':
                if type(line[1]) is int:
                    value: int = line[1]
                elif type(line[1]) is str:
                    value: int = vals[line[1]]
                    
                if value != 0:
                    # print()
                    # print(line)
                    # print(f'start val: {value}')
                    if type(line[2]) is int:
                        jump: int =  line[2]
                    else:
                        if line[2] in vals.keys():
                            jump: int =  vals[line[2]]
                    # print(jump)
                    # if jump < 0:
                    #     # try to optimize to multiplication
                    #     # print(line, vals[line[1]])
                    #     # print(data[i+jump:i])
                    #     add_vals: dict[str, int] = {}
                        
                    #     for instr in data[i+jump:i]:
                    #         if instr[0] not in ['inc', 'dec']:
                    #             i += jump
                    #             break
                    #         else:
                    #             if type(instr[1]) is str:
                    #                 if instr[0] == 'inc':
                    #                     if instr[1] in add_vals.keys():
                    #                         add_vals[instr[1]] += value
                    #                     else:
                    #                         add_vals[instr[1]] = value
                    #                 else:
                    #                     if instr[1] in add_vals.keys():
                    #                         add_vals[instr[1]] -= value
                    #                     else:
                    #                         add_vals[instr[1]] = -value
                    #             else:
                    #                 print('ERRORRRRR')
                    #     else:
                    #         for v in add_vals.keys():
                    #             print(vals)
                    #             print(add_vals)
                    #             vals[v] += add_vals[v]
                    #         i += 1
                                        
                    # else:
                    i += jump
                    continue
            elif line[0] == 'tgl':
                if type(line[1]) is int:
                    x: int = i + line[1]
                else:
                    x: int = i + vals[line[1]]
                
                if 0 <= x < len(data):
                    instr: tuple[str|int] = data[x]
                    if len(instr) == 2:
                        if instr[0] == 'inc':
                            data[x] = ('dec', *instr[1:])
                        else:
                            data[x] = ('inc', *instr[1:])
                    else:
                        if instr[0] == 'jnz':
                            data[x] = ('cpy', *instr[1:])
                        else:
                            data[x] = ('jnz', *instr[1:])
            i += 1
        return vals['a']

    def part2(self, start_a: int):
        self.part1(start_a)


d = Day23(use_example_input=0)
print(f"Part 1:\n{d.part1(start_a=7)}")
# print(f"Part 2:\n{d.part2(start_a=12)}")
