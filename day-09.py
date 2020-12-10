def ch1(preamble):
    for i in range(preamble, len(f)):
        for j in range(i-preamble, i):
            temp = f[i] - f[j]
            if temp in f[i-preamble:j] + f[j+1:i]:
                break
        else:
            return f[i]


def ch2():
    num = ch1(preamble_length)
    for i in range(len(f)-2):
        for j in range(i+1, len(f)):
            if sum(f[i:j+1]) == num:
                return min(f[i:j+1]) + max(f[i:j+1])


f = [int(x) for x in open('c:/Code/Advent of Code/2020/inputs/input9.txt').read().split('\n')]
preamble_length = 25

print(ch1(preamble_length))
print(ch2())