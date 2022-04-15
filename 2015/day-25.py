f = open('2015/inputs/input-25.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = f[0].strip('.').split()
    return (int(data[-3].strip(',')), int(data[-1]))


def part1(f):
    data = prep_input(f)
    
    num = 20151125
    # print(1, 1, num)
    
    col, row = 1, 2
    
    while True:
        if row == 0:
            row = col
            col = 1
            continue
        num = (num * 252533) % 33554393
        if col == data[1] and row == data[0]:
            return num
        col += 1
        row -= 1
            
    
    
    return data


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
