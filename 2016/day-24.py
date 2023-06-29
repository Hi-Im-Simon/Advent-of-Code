from colorama import Fore, Back, Style
import sys
sys.setrecursionlimit(int(1e6))


class Day24:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-24.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            self.data = [[int(y) if y.isnumeric() else y for y in x.rstrip()] for x in file.readlines()]
            self.start: tuple[int, int] = [(self.data[y].index(0), y) for y in range(len(self.data)) if 0 in self.data[y]][0]
            self.data = [[(-1 if char == '#' else (0 if char == '.' else char)) for char in line] for line in self.data]
            self.points: dict[int, tuple[int, int]] = {0: self.start}
            
            for y in range(len(self.data)):
                for x in range(len(self.data[y])):
                    if self.data[y][x] > 0:
                        self.points[self.data[y][x]] = (x, y)
            self.points = dict(sorted(self.points.items()))

    def part1(self):
        # self.print_maze(self.data)
        maze = self.optimize_maze([l.copy() for l in self.data])
        self.print_maze(maze)
        min_lens = {point0: {point1: sys.maxsize for point1 in self.points.keys() if point0 != point1} for point0 in self.points.keys()}
        max_skip_len = sys.maxsize # if length is higher than this value, skip
        
        def bfs(x: int, y: int, path: list[tuple[int, int]]) -> int:
            nonlocal max_skip_len
            if len(path) >= max_skip_len or len(path) > 100:
                return
            # if found a point
            if maze[y][x] > 0 and maze[y][x] != point0:
                point1 = maze[y][x]
                if len(path) < min_lens[point0][point1]:
                    min_lens[point0][point1] = len(path)
                    max_skip_len = max(min_lens[point0].values())
                    print(min_lens[point0])
            
            # all neighs
            neighs: list[tuple[int, int]] = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            
            for xx, yy in neighs:
                if (maze[yy][xx] >= 0) and ((xx, yy) not in path):
                    bfs(xx, yy, path + [(x, y)])
        
        for point0 in self.points.keys():
            bfs(*self.points[point0], [])
            break
            print('!!!!!!!!!!!!!!!!!')
                    
        return min_lens

    def part2(self):
    
        return None
    
    def optimize_maze(self, maze: list[list[int]]) -> list[list[int]]:
        visited: set[tuple[int, int]] = set()
        
        # return 1 if is a wall, 0 if not
        def bfs(x: int, y: int) -> int:
            # if is a wall
            if maze[y][x] < 0:
                return 1
            
            # all neighs
            neighs: list[tuple[int, int]] = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            
            visited.add((x, y))
            
            n_walls: int = 0
            for xx, yy in neighs:
                if (xx, yy) not in visited:
                    n_walls += bfs(xx, yy)
            
            if n_walls == 3 and maze[y][x] <= 0 and (x, y) != self.start:
                maze[y][x] = -1
                return 1
            return 0
            
        bfs(*self.start)
        
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == 0 and (x, y) not in visited:
                    maze[y][x] = -1
        return maze
    
    def print_maze(self, maze: list[list[int]]):
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                cell = maze[y][x]
                if (x, y) == self.start:
                    self.print('█', Fore.YELLOW, end='')
                elif cell == -1:
                    self.print('█', Fore.RED, end='')
                elif cell == 0:
                    self.print('.', end='')
                else:
                    self.print('█', Fore.BLUE, end='')
            print()
    
    def print(self, text: str, color: str|None = None, end: str = '\n'):
        print(f"""{color if color else ''}{text}{Fore.RESET if color else ''}""", end=end)


d = Day24(use_example_input=0)
print(f"Part 1:\n{d.part1()}")
print(f"Part 2:\n{d.part2()}")
