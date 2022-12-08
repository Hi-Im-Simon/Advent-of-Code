tf = open('2022/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2022/inputs/input-07.txt').readlines()    # your input data


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict()
        self.size = 0


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.rstrip().split() for x in f]
    sys = Directory('/', None)
    cur_dir = sys
    
    for line in data[1:]:
        if line[0] == '$':
            # command
            if line[1] == 'cd':
                if line[2] == '..':
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = cur_dir.children[line[2]]
        else:
            # data
            if line[0] != 'dir':
                cur_dir.children[f'FILE{line[1]}'] = int(line[0])
            else:
                if line[1] not in cur_dir.children.keys():
                    cur_dir.children[line[1]] = Directory(line[1], cur_dir)
                    
    def rec(el):
        if type(el) is int:
            return el
        else:
            el.size = sum([rec(s) for s in el.children.values()])
            return el.size
        
    rec(sys)
    return sys


ans_1 = 0
def part1(f):
    sys = prep_input(f)
    
    def rec(el):
        if type(el) is not int:
            if el.size <= 100000:
                global ans_1
                ans_1 += el.size
            for ch in el.children.values():
                rec(ch)
    rec(sys)
    
    return ans_1


ans_2 = float('inf')
def part2(f):
    sys = prep_input(f)
    space_needed = 30000000 - (70000000 - sys.size)
    
    def rec(el):
        if type(el) is not int:
            global ans_2
            if space_needed <= el.size < ans_2:
                ans_2 = el.size
            for ch in el.children.values():
                rec(ch)
    rec(sys)
    
    return ans_2


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
