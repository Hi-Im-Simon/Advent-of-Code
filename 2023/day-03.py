from time import time

import numpy as np


class Day3:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(
            f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-03.txt"
        ) as file:
            # edit to adjust how the program reads your files
            self.raw_data = [line.rstrip() for line in file.readlines()]
            data = ["." + line + "." for line in self.raw_data]
            self.data = ["." * len(data[0])] + data + ["." * len(data[0])]

    def find_number(self, x: int, y: int) -> tuple[str, bool]:
        max_x = x
        while True:
            if self.data[y][max_x + 1].isdigit():
                max_x += 1
            else:
                break
        str_num = self.data[y][x : max_x + 1]

        fields_to_check = (
            [(xx, y - 1) for xx in range(x - 1, max_x + 2)]
            + [(x - 1, y)]
            + [(xx, y + 1) for xx in range(x - 1, max_x + 2)]
            + [(max_x + 1, y)]
        )

        for field in fields_to_check:
            val = self.data[field[1]][field[0]]
            if not val.isdigit() and val != ".":
                return str_num, True

        return str_num, False

    def part1(self):
        ans = 0
        y = 1
        while y < len(self.data) - 1:
            line = self.data[y]
            x = 1

            while x < len(line) - 1:
                if line[x].isdigit():
                    str_num, is_adjacent = self.find_number(x, y)
                    if is_adjacent:
                        ans += int(str_num)
                    x += len(str_num)
                else:
                    x += 1
            y += 1

        return ans

    def part2(self):
        gears = []
        for y in range(len(self.raw_data)):
            for x in range(len(self.raw_data[y])):
                if self.raw_data[y][x] == "*":
                    gears.append((x + 1, y + 1))

        return gears


start = time()
d = Day3(use_example_input=True)

print(f"Part 1: {d.part1()}")
print(f"Part 2: {d.part2()}")
print(f"Time: {time() - start:.3f}s")
