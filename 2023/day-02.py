from time import time

import numpy as np


class Day2:
    def __init__(
        self, red: int, green: int, blue: int, use_example_input: bool = False
    ) -> None:
        self.available_colors = {
            "red": red,
            "green": green,
            "blue": blue,
        }
        with open(
            f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-02.txt"
        ) as file:
            # edit to adjust how the program reads your files
            self.data = [
                [
                    {
                        color_info.split()[1]: int(color_info.split()[0])
                        for color_info in set.split(",")
                    }
                    for set in line.rstrip().split(":")[1].split(";")
                ]
                for line in file.readlines()
            ]

    def _calc_game_1(self, game: list[dict[str, int]]) -> int:
        for set in game:
            for color, amount in set.items():
                if amount > self.available_colors[color]:
                    return 0
        return 1

    def part1(self):
        ans = 0
        for i, game in enumerate(self.data):
            ans += self._calc_game_1(game) * (i + 1)
        return ans

    def _calc_game_2(self, game: list[dict[str, int]]) -> int:
        colors = {"red": 0, "green": 0, "blue": 0}
        for set in game:
            for color, amount in set.items():
                if amount > colors[color]:
                    colors[color] = amount
        return colors["red"] * colors["green"] * colors["blue"]

    def part2(self):
        ans = 0
        for game in self.data:
            ans += self._calc_game_2(game)
        return ans


start = time()
d = Day2(red=12, green=13, blue=14, use_example_input=False)

print(f"Part 1: {d.part1()}")
print(f"Part 2: {d.part2()}")
print(f"Time: {time() - start:.3f}s")
