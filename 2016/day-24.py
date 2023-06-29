from colorama import Fore
import itertools, sys

sys.setrecursionlimit(int(1e6))


class Day24:
    def __init__(self, use_example_input: bool = False) -> None:
        with open(f"{__file__}/../{('example-' if use_example_input else '')}inputs/input-24.txt", 'r'
        ) as file:
            # edit to adjust how the program reads your files
            data = [[int(y) if y.isnumeric() else y for y in x.rstrip()] for x in file.readlines()]
            self.start: tuple[int, int] = [(data[y].index(0), y) for y in range(len(data)) if 0 in data[y]][0]
            data = [[(-1 if char == '#' else (0 if char == '.' else char)) for char in line] for line in data]
            self.points: dict[int, tuple[int, int]] = {0: self.start}
            
            for y in range(len(data)):
                for x in range(len(data[y])):
                    if data[y][x] > 0:
                        self.points[data[y][x]] = (x, y)
            self.points = dict(sorted(self.points.items()))
            self.maze = self.optimize_maze(data)

    def part1(self, return_to_0: bool = False):
        # self.print_maze(maze)
        dists: dict[dict[int]] = {point0: {point1: 0 for point1 in self.points.keys()} 
                                  for point0 in self.points.keys()}
        
        # calculate the matrix of distances
        for point0 in self.points.keys():
            visited: set[tuple[int, int]] = set()
            cur_points: set[tuple[int, int]] = set([self.points[point0]])
            
            path_len = 0
            while len(cur_points) > 0:
                new_points = set()
                for (x, y) in cur_points:
                    visited.add((x, y))
                    if (self.maze[y][x] > 0) and (self.maze[y][x] != point0) and (not dists[point0][self.maze[y][x]]):
                        dists[point0][self.maze[y][x]] = path_len
                        dists[self.maze[y][x]][point0] = path_len
                    
                    neighs: list[tuple[int, int]] = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for xx, yy in neighs:
                        if (self.maze[yy][xx] >= 0) and ((xx, yy) not in visited):
                            new_points.add((xx, yy))
                cur_points = new_points
                path_len += 1
        
        # generate permutations (skip first element cuz its always the starting point)
        keys = list(self.points.keys())
        keys.remove(0)
        permutations = itertools.permutations(keys)
        
        # find the shortest path
        shortest_path = sys.maxsize        
        for perm in permutations:
            # add starting point to the list
            perm = [0] + list(perm)
            # part 2: add starting point as the last to return to it
            if return_to_0: perm = perm + [0]
            
            path = 0
            for i in range(len(perm) - 1):
                path += dists[perm[i]][perm[i+1]]
            if path < shortest_path:
                shortest_path = path
                
        return shortest_path

    def part2(self):
    
        return self.part1(return_to_0=True)
    
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
