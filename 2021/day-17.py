# tf = [x.strip() for x in open('2021/inputs/input-00.txt').readlines()]
f = [x.strip() for x in open('2021/inputs/input-17.txt').readlines()]


def prep_input(f):
    f = f[0].split()[2:]
    xs = tuple([int(x) for x in f[0][2:].strip(',').split('..')])
    ys = tuple([int(x) for x in f[1][2:].strip(',').split('..')])
    return xs, ys


# probably as efficient, as possible for a bruteforce approach
def part1_and_2(f):
    # it will work only for positive x and negative y
    # I don't know if other kinds of inputs are possible in this task
    xs, ys = prep_input(f)
    ans1, ans2 = 0, 0
    
    min_vx = 0
    while sum(range(1, min_vx+1)) < xs[0]:
        min_vx += 1
        
    for vx in range(min_vx, xs[1]+1):
        for vy in range(ys[0], -ys[0]):
            # starting_velocity = (vx, vy)
            velocity = { 'x': vx, 'y': vy }
            x, y = 0, 0
            max_y = 0
            
            while x <= xs[1] and y >= ys[0]:
                max_y = max(max_y, y)
                if x >= xs[0] and y <= ys[1]:
                    ans2 += 1
                    ans1 = max(ans1, max_y)
                    break
                
                x += velocity['x']
                y += velocity['y']
                if velocity['x'] > 0:
                    velocity['x'] -= 1
                elif velocity['x'] < 0:
                    velocity['x'] += 1
                velocity['y'] -= 1  
    return ans1, ans2


ans1, ans2 = part1_and_2(f)
print(f"part 1:\n{ ans1 }")
print(f"part 2:\n{ ans2 }")
