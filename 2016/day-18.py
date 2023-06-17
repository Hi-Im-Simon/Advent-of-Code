import numpy as np


class Day18:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-18.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[int] = [0 if char == '.' else 1 for char in file.read().strip()]

    def part1(self, n_rows: int):
        safe_tiles: int = self.data.count(0)
        rows: list[list[int]] = [self.data.copy()]
        
        for _ in range(n_rows - 1):
            row = []
            for x in range(len(rows[-1])):
                if [
                    rows[-1][x-1] if x > 0 else 0,
                    rows[-1][x+1] if x < (len(rows[-1]) - 1) else 0
                ].count(1) == 1:
                    row.append(1)
                else:
                    row.append(0)
                    safe_tiles += 1
            rows.append(row)
        # [print(''.join(['^' if a == 1 else '.' for a in x[1:-1]])) for x in rows]
        return safe_tiles

    def part2(self, n_rows: int):
        return self.part1(n_rows)


d = Day18(use_example_input=False)
print(f"Part 1:\n{d.part1(40)}")
print(f"Part 2:\n{d.part2(400000)}")    # takes up to 10sec
