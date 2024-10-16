from time import time

import numpy as np


class Day1:
    digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    valid_strings = [x for x in digit_map.keys()]

    def __init__(self, use_example_input: bool = False) -> None:
        with open(
            f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-01.txt",
        ) as file:
            # edit to adjust how the program reads your files
            self.data = [line.rstrip() for line in file.readlines()]

    def part1(self):
        ans = 0
        for line in self.data:
            first, last = None, None

            for i in range(len(line)):
                if (not first) and line[i].isdigit():
                    first = line[i]
                if (not last) and line[-i - 1].isdigit():
                    last = line[-i - 1]

                if first and last:
                    ans += int(first + last)
                    break
            else:
                exit(f"!!! No solution found in: {line}")
        return ans

    def part2(self):
        ans = 0
        for line in self.data:
            rev_line = line[::-1]
            first, last = None, None

            for i in range(len(line)):
                if not first:
                    if line[i].isdigit():
                        first = line[i]
                    else:
                        for j in range(0, i):
                            if line[j : i + 1] in self.valid_strings:
                                first = self.digit_map[line[j : i + 1]]
                if not last:
                    if rev_line[i].isdigit():
                        last = rev_line[i]
                    else:
                        for j in range(0, i):
                            rev_string = rev_line[j : i + 1][::-1]
                            if rev_string in self.valid_strings:
                                last = self.digit_map[rev_string]

                if first and last:
                    ans += int(first + last)
                    break
            else:
                exit(f"!!! No solution found in: {line}")
        return ans


start = time()
d = Day1(use_example_input=False)

print(f"Part 1: {d.part1()}")
print(f"Part 2: {d.part2()}")
print(f"Time: {time() - start:.3f}s")
