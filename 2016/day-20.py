MIN_VAL = 0
MAX_VAL = 4294967295
# MAX_VAL = 220


class Day20:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-20.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.rangs: list[tuple[int, int]] = sorted([tuple(map(int, x.rstrip().split('-'))) for x in file.readlines()])
            
    def get_better_rangs(self):
        self.new_rangs: list[tuple[int, int]] = []
        cur_x, cur_y = self.rangs[0]
        
        for x, y in self.rangs[1:]:
            if x <= (cur_y + 1):
                cur_y = max(cur_y, y)
            else:
                self.new_rangs.append((cur_x, cur_y))
                cur_x, cur_y = x, y
        # include last rang
        self.new_rangs.append((cur_x, cur_y))

    def part1(self):
        return (self.new_rangs[0][1] + 1) if self.new_rangs[0][0] == MIN_VAL else MIN_VAL

    def part2(self):
        ans = 0
        cur = MIN_VAL - 1
        for x, y in self.new_rangs:
            ans += (x - cur - 1)
            cur = y
        return ans + (MAX_VAL - cur)


d = Day20(use_example_input=0)
d.get_better_rangs()
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
