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

    def part1(self):
        self.print_maze(self.data)
        maze = self.optimize_maze([l.copy() for l in self.data])
        # self.print_maze(maze)
    
        return None

    def part2(self):
    
        return None
    
    def optimize_maze(self, maze: list[list[int]]) -> list[list[int]]:
        visited: set[tuple[int, int]] = set()
        weirds = set()
        
        # return 1 if is a wall, 0 if not
        def bfs(x: int, y: int) -> int:
            # if is a wall
            if maze[y][x] < 0:
                return 1
            
            # all neighs
            neighs: list[tuple[int, int]] = [(xx, yy) for (xx, yy) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]]
            
            visited.add((x, y))
            
            n_walls: int = 0
            for xx, yy in neighs:
                if (xx, yy) not in visited:
                    n_walls += bfs(xx, yy)
            
            if n_walls == 3 and maze[y][x] <= 0:
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
