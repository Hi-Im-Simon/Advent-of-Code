def ch1(ans1=0, ans3=0):
    for i in range(1, len(f)):
        dif = f[i] - f[i-1]
        if dif == 1:
            ans1 += 1
        if dif == 3:
            ans3 += 1
    return ans1 * ans3


def ch2():
    for i in range(2, len(f)-1):
        if f[i+1] - f[i-2] == 3:
            print(f[:i-1] + f[i+1:])



f = [0] + sorted([int(x) for x in open('c:/Code/Advent of Code/2020/inputs/input-10.txt').read().split('\n')])
f += [f[-1] + 3]

print(ch1())
print(ch2())