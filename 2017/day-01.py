import numpy as np


class Day1:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-01.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[str] = list(file.read())

    def part1(self):
        ans: int = 0
        for i in range(-1, len(self.data)-1):
            if self.data[i] == self.data[i+1]:
                ans += int(self.data[i])
        return ans

    def part2(self):
        ans: int = 0
        jump: int = len(self.data) // 2
        for i in range(0, jump):
            if self.data[i] == self.data[i+jump]:
                ans += (int(self.data[i]) * 2)
        return ans


d = Day1(use_example_input=0)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
