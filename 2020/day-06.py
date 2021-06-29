file = open('2020/inputs/input-06.txt')
f = [x.strip() for x in file.readlines()]
i = 1
f[0] = [f[0]]
while len(f) > i:
    if f[i] == '':
        f[i] = []
        i += 1
    else:
        f[i - 1].append(f[i])
        del f[i]


def sum_of_counts(file):
    ans = 0
    for group in file:
        answers = []
        for member in group:
            for answer in member:
                if answer not in answers:
                    answers.append(answer)
        ans += len(answers)
    return ans


def sum_of_common_counts(file):
    ans = 0
    for group in file:
        answers = list(group[0])
        i = 0
        while i < len(answers):
            for member in group:
                if answers[i] not in member:
                    answers.remove(answers[i])
                    i -= 1
                    break
            i += 1
        ans += len(answers)
    return ans


print(sum_of_counts(f))
print(sum_of_common_counts(f))

file.close()
