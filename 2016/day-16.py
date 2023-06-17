import numpy as np


class Day16:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-16.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[str] = list(file.read().strip())

    def part1(self, disk_len: int):
        a: list[str] = self.data.copy()
        while len(a) < disk_len:
            a = a + ['0'] + ['0' if char == '1' else '1' for char in a[::-1]]
        
        checksum: list[str] = a[:disk_len]
        while not (len(checksum) % 2):
            checksum = ['1' if checksum[i] == checksum[i+1] else '0'
                        for i in range(0, len(checksum), 2)]
        return ''.join(checksum)

    def part2(self, disk_len: int):
        return self.part1(disk_len)


d = Day16(use_example_input=False)
print(f"Part 1:\n{d.part1(272)}")
print(f"Part 2:\n{d.part2(35651584)}")
