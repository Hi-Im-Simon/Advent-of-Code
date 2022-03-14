from math import sqrt


tf = open('2021/inputs/input-00.txt').readlines()   # you can put an example input data here
f = open('2021/inputs/input-19.txt').readlines()    # your input data


def prep_input(f):  # edit to adjust how the program reads your files
    data = [x.strip() for x in f]
    out = []
    i = -1
    for line in data:
        if line[0:3] == '---':
            i += 1
            out.append([])
        elif line == '':
            continue
        else:
            out[i].append([int(x) for x in line.split(',')])
    return out


def part1(f):
    data = prep_input(f)
    ref_data = []
    
    for s, scanner in enumerate(data):
        ref_data.append([])
        for i in range(len(scanner) - 1):
            for j in range(i + 1, len(scanner)):
                x, y, z = [abs(scanner[i][t] - scanner[j][t]) for t in range(3)]
                ref_data[s].append([sqrt(y**2 + sqrt(x**2 + z**2)**2), (i, j)])
    
    current, available = 0, [x for x in range(1, len(data))]
    
    while len(available):
        for other in available:
            count = 0
            cur, new = ref_data[current], ref_data[other]
            
            for el1 in new:
                for el2 in cur:
                    if el1[0] == el2[0]:
                        count += 1
                        element_new = el1[1]
                        element_old = el2[1]
                        # print(data[current][element_old[0]], data[current][element_old[1]])
                        # print(data[other][element_new[0]], data[other][element_new[1]])
            
            if count >= 66:
                
                diffr_table_old = [data[current][element_old[0]][z] - data[current][element_old[1]][z] for z in range(3)]
                diffr_table_new = [data[other][element_new[0]][z] - data[other][element_new[1]][z] for z in range(3)]
                print(data[current][element_old[0]], data[current][element_old[1]], diffr_table_old)
                print(data[other][element_new[0]], data[other][element_new[1]], diffr_table_new)
                order_table = []
                for i in range(len(diffr_table_old)):
                    for j in range(len(diffr_table_new)):
                        if abs(diffr_table_old[i]) == abs(diffr_table_new[j]):
                            order_table.append(j)                        
                neg_table = [1 if diffr_table_old[i] == diffr_table_new[i] else -1 for i in range(3)]
                
                print(order_table, neg_table)
                
                old_el = data[current][element_old[0]]
                new_el = [data[other][element_new[0]][i] * neg_table[i] for i in order_table]
                
                for i in range(3):
                    print(-(diffr_table_old[i] - old_el[i] - new_el[i]))
                
                print(old_el)
                print(new_el)
                
                
                
                current = other
                available.remove(other)
                print(available)
                break
    
    return


def part2(f):
    data = prep_input(f)
    
    
    return None


print(f"part 1:\n{ part1(tf) }")
print(f"part 2:\n{ part2(f) }")
