import numpy as np


class Day3:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-03.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data = int(file.read())
            self.data = 2

    def part1(self):
        
        bottom_right_val: int = 1
        ring_n: int = 0
        
        while True:
            next_val: int = bottom_right_val + (ring_n + 1)*8
            if next_val <= self.data:
                pass
            else:
                ring_n += 1
                bottom_right_val = next_val
            
        return bottom_right_val, ring_n

    def part2(self):
        
    
        return None


d = Day3(use_example_input=0)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
