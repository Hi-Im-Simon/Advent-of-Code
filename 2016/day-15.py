import numpy as np


class Day15:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-15.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            data = [x.rstrip().split() for x in file.readlines()]
            self.data: list[dict[str, int]] = [{
                'n_pos': int(d[3]),
                'pos_0': (int(d[-1].rstrip('.')) - int(d[6].split('=')[1].rstrip(','))) % int(d[3])
            } for d in data]

    def part1(self, data: list[dict[str, int]] | None = None):
        if data == None:
            data = self.data
        
        wait_time = 0
        while True:
            for i, disc in enumerate(data):
                cur_fall_time = i + 1
                cur_disc_pos = (disc['pos_0'] + cur_fall_time + wait_time) % disc['n_pos']
                if cur_disc_pos != 0:
                    wait_time += 1
                    break
            else:
                return wait_time

    def part2(self):
        data = self.data + [{'n_pos': 11, 'pos_0': 0}]
        return self.part1(data)


d = Day15(use_example_input=False)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
