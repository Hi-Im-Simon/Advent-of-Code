import numpy as np
from hashlib import md5
import sys


sys.setrecursionlimit(3000)
shortest_path_len: int = sys.maxsize
shortest_path_code: list[str] = []
longest_path_len: int = 0


class Day17:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-17.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.base_code: list[str] = list(file.read().strip())

    def get_hash(self, code: list[str]) -> list[str]:
        return list(md5(''.join(code).encode('utf-8')).hexdigest())
    
    def create(self):
        end_x, end_y = 3, 3
        
        def rec(cur_code: list[str], x: int, y: int, path_len: int = 0):
            paths: list[bool] = [True if c in ['b', 'c', 'd', 'e', 'f'] else False for c in self.get_hash(cur_code)[:4]]
            
            if x == end_x and y == end_y:
                global shortest_path_len, shortest_path_code, longest_path_len
                if path_len < shortest_path_len:
                    shortest_path_len = path_len
                    shortest_path_code = cur_code
                if path_len > longest_path_len:
                    longest_path_len = path_len
                    
            else:
                path_len += 1
                # up
                if paths[0] and 0 < y:
                    rec(cur_code + ['U'], x, y-1, path_len)
                # down
                if paths[1] and y < (end_y):
                    rec(cur_code + ['D'], x, y+1, path_len)
                # left
                if paths[2] and 0 < x:
                    rec(cur_code + ['L'], x-1, y, path_len)
                # right
                if paths[3] and x < (end_x):
                    rec(cur_code + ['R'], x+1, y, path_len)
        
        rec(self.base_code, 0, 0)
    
    def part1(self):
        return ''.join(shortest_path_code).lstrip(''.join(self.base_code))

    def part2(self):
        return longest_path_len


d = Day17(use_example_input=False)
d.create()
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
