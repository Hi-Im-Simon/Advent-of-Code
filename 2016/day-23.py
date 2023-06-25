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
        
        # instructions' functions
        def cpy(line: tuple[str|int]):
            if type(line[2]) is str:
                if type(line[1]) is int:
                    vals[line[2]] = line[1]
                else:
                    if line[1] in vals.keys():
                        vals[line[2]] = vals[line[1]]
        
        def inc(line: tuple[str|int], by: int=1):
            if line[1] in vals.keys():
                vals[line[1]] += by
                
        def dec(line: tuple[str|int], by: int=1):
            if line[1] in vals.keys():
                vals[line[1]] -= by
                
        def tgl(line: tuple[str|int]):
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
        
        # returns by how many positions the cursor should jump
        def jnz(line: tuple[str|int]) -> int:
            # get the value (which is also a loop length)
            if type(line[1]) is int:
                value: int = line[1]
            elif type(line[1]) is str:
                value: int = vals[line[1]]
                
            if value != 0:
                if type(line[2]) is int:
                    jump: int =  line[2]
                else:
                    if line[2] in vals.keys():
                        jump: int =  vals[line[2]]
                
                if jump < 0:
                    jump_lines = data[i+jump:i]
                    # if len = 2, only inc and/or dec instructions, complete both
                    if len(jump_lines) == 2:
                        for temp_line in jump_lines:
                            if temp_line[0] == 'inc':
                                inc(temp_line, value)
                            elif temp_line[0] == 'dec':
                                dec(temp_line, value)
                        return 1
                    
                    # if len = 5, `a` will be incresed by (outher_loop_len * inner_loop_len)
                    # other variables don't matter (will be overwritten anyways)
                    elif len(jump_lines) == 5:
                        if type(jump_lines[0][1]) is str:
                            vals['a'] += (vals[jump_lines[0][1]] * value)
                        else:
                            vals['a'] += (jump_lines[0][1] * value)
                        return 1
                    
                    # there aren't many loops of other sizes, so there is no reason to optimize them (< 10 executions)
                    # so just execute them
                    return jump
                else:
                    return jump
            return 1
        
        # main loop
        while i < len(data):
            line: tuple[str|int] = data[i]
            jump_by: int = 1
            # print(line, {key: vals[key] for key in line if key in vals.keys()})
            
            if line[0] == 'cpy':
                cpy(line)
            elif line[0] == 'inc':
                inc(line)
            elif line[0] == 'dec':
                dec(line)
            elif line[0] == 'jnz':
                jump_by = jnz(line)
            elif line[0] == 'tgl':
                tgl(line)
                
            i += jump_by
        return vals['a']

    def part2(self, start_a: int):
        return self.part1(start_a)


d = Day23(use_example_input=0)
print(f"Part 1:\n{d.part1(start_a=7)}")
print(f"Part 2:\n{d.part2(start_a=12)}")
