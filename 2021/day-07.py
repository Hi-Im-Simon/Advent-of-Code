from statistics import median

# tf = [int(x) for x in open('2021/inputs/input-00.txt').readlines()[0].split(',')]
f = [int(x) for x in open('2021/inputs/input-07.txt').readlines()[0].split(',')]


def part1(f):
	ans, go_to = 0, round(median(f))
	for el in f:
		ans += abs(el - go_to)
	return ans


def part2(f):
	go_to = int(sum(f) / len(f))
	ans = 0
	for el in f:
		for i in range(1, abs(el-go_to)+1):
			ans += i
	return ans


print('part 1:\n' + str(part1(f)))
print('part 2:\n' + str(part2(f)))
