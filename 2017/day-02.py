import numpy as np


class Day2:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-02.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data = [tuple(map(int, x.rstrip().split())) for x in file.readlines()]

    def part1(self):
        return sum([max(line) - min(line) for line in self.data])

    def part2(self):
        return int(sum([self.check_line(line) for line in self.data]))
    
    def check_line(self, line: tuple[int]) -> int:
        for i in range(len(line)):
            for j in range(len(line)):
                if i != j:
                    if not (line[i] % line[j]):
                        return line[i] / line[j]
                    if not (line[j] % line[i]):
                        return line[j] / line[i]
        return 0


d = Day2(use_example_input=0)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
