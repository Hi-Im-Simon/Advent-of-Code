tf = open('2021/inputs/input-00.txt').readlines()[0].strip()
f = open('2021/inputs/input-16.txt').readlines()[0].strip()


def when_type1_4(string):
    val = ''
    while int(string[0]):
        val += string[1:5]
        string = string[5:]
    val += string[1:5]
    string = string[5:]
    # val to be used later?
    return string, int(val, 2)

def when_type2_0(string):
    val = int(string[:15], 2)
    string = string[15:]
    # val to be used later?
    return string, val
    
def when_type2_1(string):
    val = int(string[:11], 2)
    string = string[11:]
    # val to be used later?
    return string, val


def part1(f):
    ans = 0
    string = ''.join(['0' * (4-len(x)) + x for x in [bin(int(x, 16))[2:] for x in list(f)]])
    
    while not string == '' and int(string, 2) > 0:
        ans += int(string[:3], 2)
        type1 = int(string[3:6], 2)
        string = string[6:]
        if type1 == 4:
            string, _ = when_type1_4(string)
        else:
            type2 = int(string[0])
            string = string[1:]
            if type2:
                string, _ = when_type2_1(string)
            else:
                string, _ = when_type2_0(string)
    return ans


# def part2(f):
#     ans = 0
#     string = ''.join(['0' * (4-len(x)) + x for x in [bin(int(x, 16))[2:] for x in list(f)]])
    
#     while not string == '' and int(string, 2) > 0:
#         print(string)
#         type1 = int(string[3:6], 2)
#         string = string[6:]
#         print(string, type1)
#         if type1 == 4:
#             string, _ = when_type1_4(string)
#         else:
#             type2 = int(string[0])
#             string = string[1:]
#             if type2:
#                 string, subp_count = when_type2_1(string)
#             else:
#                 string, subp_length = when_type2_0(string)
#     return ans


print(f"part 1:\n{ part1(f) }")
# print(f"part 2:\n{ part2(tf) }")
