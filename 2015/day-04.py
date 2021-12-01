import hashlib as hl
import threading as th
import time


tf = open('2015/inputs/input-00.txt').read()
f = open('2015/inputs/input-04.txt').read()

ans = 0
found = 0


def look(zeroes, x1, x2):
    global found
    if found == 0 and len(zeroes) == 5 or found == 1 and len(zeroes) == 6:
        for i in range(x1, x2):
            out = hl.md5((f + str(i)).encode()).hexdigest()
            if out[:len(zeroes)] == zeroes:
                found += 1
                print('part ' + str(len(zeroes) - 4) + ':\n' + str(i))
                

def md5_hash(zeroes, s):
    global found
    i = 0
    while found == 0 and len(zeroes) == 5 or found == 1 and len(zeroes) == 6:
        th.Thread(target=look, args=(zeroes, i, i+s)).start()
        i += s
        time.sleep(0.1)


md5_hash('00000', 100000)
md5_hash('000000', 100000)
