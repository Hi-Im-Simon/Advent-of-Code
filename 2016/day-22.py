from colorama import Fore, Back, Style
import numpy as np


class Day22:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-22.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data: list[list[dict[str, float|int]]] = []
            for line in file.readlines()[2:]:
                line = line.rstrip().split()
                x, y = [int(c[1:]) for c in line[0].split('-')[1:]]
                if x == 0:
                    self.data.append([])
                self.data[y].append({
                    'size': int(line[1][:-1]),
                    'used': int(line[2][:-1]),
                    'avail': int(line[3][:-1]),
                    'use%': int(line[4][:-1]) / 100,
                })

    def part1(self):
        # used - if you can hold [KEY]T, then you can hold [VALUE] elements
        used: dict[int, int] = {}
        
        for row in self.data:
            for node in row:
                if node['used'] > 0:
                    if node['used'] not in used:
                        used[node['used']] = 1
                    else:
                        used[node['used']] += 1
        used = dict(sorted(used.items()))
        
        # for i, size in enumerate(list(sizes.keys())[::-1]):
        #     i = len(sizes) - i - 1
        #     sizes[size] += sum(list(sizes.values())[:i])
        sum_can_fit: int = 0
        for row in self.data:
            for node in row:
                can_fit: int = 0
                for use in used.keys():
                    if node['avail'] >= use:
                        can_fit += used[use]
                    else:
                        # remove self
                        if use >= node['used'] and node['used'] > 0:
                            can_fit -= 1
                        break
                if can_fit > 0:
                    sum_can_fit += can_fit
        return sum_can_fit

    def node_av(self, node: dict[str, int]):
        return node['size'] - node['used']
    
    def part2(self, prints=False):
        data: np.ndarray[np.ndarray[dict[str, int]]] = np.array([[{key: node[key] for key in node.keys()} for node in row] for row in self.data])
        actions: int = 0
        
        # coords of the empty spot
        x, y = None, None # (x, y)
        
        # finds the empty spot and removes all rows below
        def remove_rows() -> tuple[int, int]:
            nonlocal data
            coords = None
            for y in range(len(data)):
                if not coords:
                    for x in range(len(data[y])):
                        if data[y, x]['used'] == 0:
                            coords = (x, y)
                            data = np.delete(data, np.s_[max(y+1, 2):], 0)
                            break
                else: break
            return coords
            
        def swap(xy0: tuple[int, int], xy1: tuple[int, int]) -> None:
            data[xy0[::-1]], data[xy1[::-1]] = data[xy1[::-1]], data[xy0[::-1]]
            
        (x, y) = remove_rows()
        
        # find walls
        for _y in range(len(data)):
            for _x in range(len(data[_y])):
                if data[_y, _x]['size'] > 100:
                    data[_y, _x]['is_wall'] = True
                else:
                    data[_y, _x]['is_wall'] = False
                    
        if prints: self.print_mat(data, 0)
        # get the empty point to (x=N-2 y=0)
        while (x, y) != (len(data[0]) - 2, 0):
            # try to go up or dodge walls
            if y > 1:
                if data[y-1, x]['is_wall']:
                    # might need to adjust this for other kind of inputs
                    # go left
                    swap((x, y), (x-1, y))
                else:
                    swap((x, y), (x, y-1))
            else:
                if x < (len(data[0]) - 2):
                    # go right
                    swap((x, y), (x+1, y))
                else:
                    # go up to the final point
                    swap((x, y), (x, y-1))
                    
            (x, y) = remove_rows()
            actions += 1
            if prints:
                print()
                self.print_mat(data, actions)
        
        # we can easily calculate the remaining number of actions needed
        return actions + (5 * (len(data[0]) - 2)) + 1

    def print_mat(self, data: np.ndarray[np.ndarray[dict[str, int]]]|list[list[dict[str, float | int]]], action_n: int|None = None):
        if action_n != None:
            print(f"Action {action_n}:")
        for y in range(len(data)):
            for x in range(len(data[y])):
                node = data[y][x]
                text: str = ''
                color: str|None = None
                
                if node['used'] == 0:
                    text = f"__/{node['size']}"
                elif node['size'] > 100:
                    text = 'XXXXX'
                    color = Fore.RED
                else:
                    text = f"{node['used']}/{node['size']}"
                
                for yy, xx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    try:
                        if node['avail'] >= data[y + yy][x + xx]['used'] and data[y + yy][x + xx]['used'] > 0:
                            color = Fore.GREEN
                    except Exception:
                        continue
                
                self.print(text, color, end=' ')
            print()
        
    def print(self, text: str, color: str|None = None, end: str = '\n'):
        print(f"""{color if color else ''}{text}{Fore.RESET if color else ''}""", end=end)
        

d = Day22(use_example_input=False)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2(prints=False)}")
