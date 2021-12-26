# tf = open('2021/inputs/input-00.txt').readlines()[0].strip()
f = open('2021/inputs/input-16.txt').readlines()[0].strip()


def when_type1_4(string):
    val = ''
    while int(string[0]):
        val += string[1:5]
        string = string[5:]
    val += string[1:5]
    string = string[5:]
    return string, int(val, 2)


def when_type2_0(string):
    val = int(string[:15], 2)
    string = string[15:]
    return string, val
    
    
def when_type2_1(string):
    val = int(string[:11], 2)
    string = string[11:]
    return string, val


def get_type1(string):
    global ans1
    ans1 += int(string[:3], 2)
    type1 = int(string[3:6], 2)
    string = string[6:]
    return string, type1


def get_type2(string):
    type2 = int(string[0])
    string = string[1:]
    return string, type2


def rec(string, packet_len=float('inf')):
    ans = []
    while not string == '' and int(string, 2) > 0 and packet_len > 0:
        packet_len -= 1
        string, type1 = get_type1(string)
        if type1 == 4:
            string, val = when_type1_4(string)
            ans.append(val)
        else:
            string, type2 = get_type2(string)
            if type2 == 0:
                string, length = when_type2_0(string)
                new_string = string[:length]
                string = string[length:]
                rec_val = rec(new_string)
            else:
                string, count = when_type2_1(string)
                rec_val, string = rec(string, count)
            match type1:
                case 0: ans.append(sum(rec_val))
                case 1: 
                    t = rec_val[0]
                    for r in rec_val[1:]:
                        t *= r
                    ans.append(t)
                case 2: ans.append(min(rec_val))
                case 3: ans.append(max(rec_val))
                case 5: ans.append(1 if rec_val[0] > rec_val[1] else 0)
                case 6: ans.append(1 if rec_val[0] < rec_val[1] else 0)
                case 7: ans.append(1 if rec_val[0] == rec_val[1] else 0)
    if packet_len == 0:
        return ans, string
    return ans


def part1(f):
    string = ''.join(['0' * (4-len(x)) + x for x in [bin(int(x, 16))[2:] for x in list(f)]])
    rec(string)[0]
    return ans1


def part2(f):
    string = ''.join(['0' * (4-len(x)) + x for x in [bin(int(x, 16))[2:] for x in list(f)]])
    ans = rec(string)[0]
    return ans


ans1 = 0

print(f"part 1:\n{ part1(f) }")
print(f"part 2:\n{ part2(f) }")
