tf = [x.strip().strip('.').split() for x in open('2015/inputs/input-00.txt').readlines()]
f = [x.strip().strip('.').split() for x in open('2015/inputs/input-14.txt').readlines()]


class Raindeer:
    def __init__(self, speed, run_time, rest_time):
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time
        self.resting_for = 0
        self.dist_travelled = 0
        self.time_travelled = 0


def prep_input(f):
    rains = {}
    for line in f:
        rains[line[0]] = Raindeer(int(line[3]), int(line[6]), int(line[13]))
    return rains


def simulate(f, t):
    rains = prep_input(f)
    dists = []
    for rain in rains:
        rain = rains[rain]
        tt = 0
        dist = 0
        while tt <= t:
            dist += min(rain.speed * rain.run_time, rain.speed * (t - tt))
            tt += rain.run_time + rain.rest_time
        dists.append(dist)
    return max(dists)
    
    
def simulate_points(f, t):
    rains = prep_input(f)
    points = {r: 0 for r in rains}
    for _ in range(t):
        max_dist = 0
        for rain in rains:
            r = rains[rain]
            if r.resting_for:
                r.resting_for -= 1
            elif r.time_travelled >= r.run_time:
                r.resting_for = r.rest_time - 1
                r.time_travelled = 0
            else:
                r.dist_travelled += r.speed
                r.time_travelled += 1
            if r.dist_travelled == max_dist:
                leading.append(rain)
            elif r.dist_travelled > max_dist:
                max_dist = r.dist_travelled
                leading = [rain]
        for l in leading:
            points[l] += 1
    return max(points.values())


print('part 1:\n' + str(simulate(f, 2503)))
print('part 2:\n' + str(simulate_points(f, 2503)))
