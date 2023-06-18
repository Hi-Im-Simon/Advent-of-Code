import numpy as np


class Day19:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-19.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.n_elves = int(file.read())
            # self.n_elves = 11

    def part1(self):
        elves: list[int] = list(range(1, self.n_elves+1))
        start_from: bool = 0
        next_start_from: bool = 0
        while len(elves) > 1:
            if len(elves) % 2:
                next_start_from = (not next_start_from)
            elves = [elves[i] for i in range(start_from, len(elves), 2)]
            start_from = next_start_from
        return elves[0]

    def part2(self):
        elves: list[int] = list(range(1, self.n_elves+1))
        while len(elves) > 1:
            last_size: int = len(elves)
            half = int(len(elves) / 2)
            elves = elves[:half] + elves[half+(1 if (len(elves) % 2) else 2)::3]
            
            next_elf_pos = (last_size - len(elves)) % len(elves)
            
            elves = elves[next_elf_pos:] + elves[:next_elf_pos]
        return elves[0]


d = Day19(use_example_input=False)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
