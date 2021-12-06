# tf = [int(x.strip()) for x in open('2015/inputs/input-00.txt').readlines()]
f = [int(x.strip()) for x in open('2015/inputs/input-17.txt').readlines()]

using_c_dict = {}


def fill_ups(conts, go_to, cur=0, using_c=0):
    if cur > go_to: return 0
    elif cur == go_to:
        global using_c_dict
        if using_c in using_c_dict:
            using_c_dict[using_c] += 1
        else:
            using_c_dict[using_c] = 1
        return 1
    ans = 0
    for i, cont in enumerate(conts):
        new_conts = conts.copy()
        new_conts = new_conts[i+1:]
        ans += fill_ups(new_conts, go_to, cur+cont, using_c+1)
    return ans


def min_container_count():
    global using_c_dict
    return using_c_dict[min(using_c_dict)]


print('part 1:\n' + str(fill_ups(f, 150)))
print('part 2:\n' + str(min_container_count()))
