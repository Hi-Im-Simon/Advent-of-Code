# tf = eval([x.strip() for x in open('2015/inputs/input-00.txt').readlines()][0])
f = eval([x.strip() for x in open('2015/inputs/input-12.txt').readlines()][0])


def search_dict(d, ignore_word=None):
    count = 0
    for x in d.values():
        tp = type(x)
        if tp is int:
            count += x
        elif tp is dict:
            count += search_dict(x, ignore_word)
        elif tp is list:
            count += seatch_list(x, ignore_word)
        elif tp is str:
            if x == ignore_word:
                return 0
        else:
            print(x)
    return count
    
    
def seatch_list(l, ignore_word=None):
    count = 0
    for x in l:
        tp = type(x)
        if tp is int:
            count += x
        elif tp is dict:
            count += search_dict(x, ignore_word)
        elif tp is list:
            count += seatch_list(x, ignore_word)
        elif tp is str:
            pass
        else:
            print(x)
    return count


def count_all_nums(f, ignore_word=None):
    count = 0
    for x in f:
        tp = type(x)
        if tp is dict:
            count += search_dict(x, ignore_word)
        elif tp is list:
            count += seatch_list(x, ignore_word)
        else:
            print(x)
    return count


print('part 1:\n' + str(count_all_nums(f)))
print('part 2:\n' + str(count_all_nums(f, 'red')))
