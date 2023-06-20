import numpy as np


class Day21:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-21.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[str] = [x.rstrip().split() for x in file.readlines()]
        
    def swap(self, string: str, instr: list[str]):
        if instr[1] == 'position':
            x, y = int(instr[2]), int(instr[5])
        elif instr[1] == 'letter':
            x, y = string.index(instr[2]), string.index(instr[5])
        string[x], string[y] = string[y], string[x]
        return string
    
    def reverse(self, string: str, instr: list[str]):
        x, y = int(instr[2]), int(instr[4])
        string[x:y+1] = string[x:y+1][::-1]
        return string      

    def part1(self, string: str):
        string: list[str] = list(string)
        for instr in self.data:
            # swap
            if instr[0] == 'swap':
                string = self.swap(string, instr)
            # rotate
            elif instr[0] == 'rotate':
                if instr[1] == 'based':
                    x: int = (string.index(instr[6]) + 1 + (1 if string.index(instr[6]) >= 4 else 0)) % len(string)
                else:
                    x: int = int(instr[2]) % len(string)
                if instr[1] == 'left':
                    string = string[x:] + string[:x]
                elif instr[1] in ['right', 'based']:
                    string = string[-x:] + string[:-x]
            # reverse
            elif instr[0] == 'reverse':
                string = self.reverse(string, instr)
            # move
            elif instr[0] == 'move':
                x, y = int(instr[2]), int(instr[5])
                string.insert(y, string.pop(x))
        return ''.join(string)

    def part2(self, string: str):
        string: list[str] = list(string)
        for instr in self.data[::-1]:
            # un-swap
            if instr[0] == 'swap':
                string = self.swap(string, instr)
            # un-rotate
            elif instr[0] == 'rotate':
                if instr[1] == 'based':
                    # x: int = (string.index(instr[6]) + 1 + (1 if string.index(instr[6]) >= 4 else 0)) % len(string)
                    is_at: int = string.index(instr[6])
                    for i in range(len(string)):
                        rot = (i + (1 + (1 if i >= 4 else 0)))
                        new_pos = (i + rot) % len(string)
                        if new_pos == is_at:
                            x: int = rot % len(string)
                else:
                    x: int = int(instr[2]) % len(string)
                if instr[1] == 'left':
                    string = string[-x:] + string[:-x]
                elif instr[1] in ['right', 'based']:
                    string = string[x:] + string[:x]
            # un-reverse
            elif instr[0] == 'reverse':
                string = self.reverse(string, instr)
            # un-move
            elif instr[0] == 'move':
                x, y = int(instr[2]), int(instr[5])
                string.insert(x, string.pop(y))
        return ''.join(string)


d = Day21(use_example_input=0)
print(f"Part 1:\n{d.part1('abcdefgh')}")
print(f"Part 2:\n{d.part2('fbgdceah')}")
