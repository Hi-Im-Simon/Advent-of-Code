tf = list([x.strip() for x in open('2015/inputs/input-00.txt').readlines()][0])
f = list([x.strip() for x in open('2015/inputs/input-11.txt').readlines()][0])


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
bad_letters = [letters.index('i'), letters.index('o'), letters.index('l')]


def up_letter(passw, i=-1):
    if passw[i] + 1 == len(letters):
        passw[i] = 0
        passw = up_letter(passw, i-1)
    else:
        passw[i] += 1
    return passw


def validate(passw):
    for i in range(3, len(passw)+1):
        el = passw[-i]
        if passw[-i+1] == el + 1 and passw[-i+2] == el + 2:
            break
    else:
        return False
    i = 1
    c = 0
    while i < len(passw):
        if passw[i] == passw[i-1]:
            c += 1
            i += 1
        i += 1
    if c < 2:
        return False
    return True


def new_password(passw):
    passw = [letters.index(x) for x in passw]
    while True:
        passw = up_letter(passw)
        for l in range(len(passw)):
            if passw[l] in bad_letters:
                passw[l] += 1
        if validate(passw):
            return ''.join([letters[x] for x in passw])
    

new_p = new_password(f)
print('part 1:\n' + str(new_p))
print('part 2:\n' + str(new_password(new_p)))
