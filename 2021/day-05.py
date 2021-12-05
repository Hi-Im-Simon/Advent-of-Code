tf = [[tuple(map(int, y.split(','))) for y in x.strip().split(' -> ')] for x in open('2021/inputs/input-00.txt').readlines()]
f = [[tuple(map(int, y.split(','))) for y in x.strip().split(' -> ')] for x in open('2021/inputs/input-05.txt').readlines()]


def list_points(f, type):
    points = []
    for line in f:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            x1, x2 = sorted([line[0][0], line[1][0]])
            y1, y2 = sorted([line[0][1], line[1][1]])
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    points.append((x, y))
        elif type == 'full':
            x1, x2 = [line[0][0], line[1][0]]
            y1, y2 = [line[0][1], line[1][1]]
            if x1 > x2:
                x1, x2, y1, y2 = x2, x1, y2, y1
            for i in range(x2-x1+1):
                if y1 <= y2:
                    points.append((x1+i, y1+i))
                else:
                    points.append((x1+i, y1-i))
    return points


def create_overlap_list(size):
    ov_list = [[0 for _ in range(size)] for _ in range(size)]
    return ov_list


def find_overlaps(f, type='full', size=10):
    ans = 0
    points = list_points(f.copy(), type)
    ov_list = create_overlap_list(size)
    for p in points:
        ov_list[p[1]][p[0]] += 1
    for y in ov_list:
        for x in y:
            if x > 1:
                ans += 1
    return ans

        
print('part 1:\n' + str(find_overlaps(f, 'linear', 1000)))
print('part 2:\n' + str(find_overlaps(f, 'full', 1000)))
