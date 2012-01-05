
import sys
import os
import heapq
from myhash import *


def main():
    """ USAGE: e.g., python2.7 distinctNvectors.py 3 test.txt """
    MyH = MyHash()
    if (len(sys.argv) < 3):
        print main.__doc__
        return
    N = int(sys.argv[1])
    h = []
    f = open(sys.argv[2], 'r')
    counts = {}

    start = 0
    lastreadline = -1



    while True:
        if len(counts) < N:
            while True:
                tmp = getnextline(f)
                lastreadline += 1
                if tmp != '\n':
                    break
            if tmp == '':
                break
            port = (int(tmp.rstrip()))
            if port in counts:
                counts[port] += 1
            else:
                counts[port] = 1
            heapq.heappush(h, (lastreadline, port))
        
        else:
            distinctvector = get_distinct(N, h)
            
            for p in distinctvector:
                print(p),

            u64 = MyH.changeVec16toU64(distinctvector)
            print('; ' + str(u64))

            tmp = heapq.heappop(h)
            counts[tmp[1]] -= 1
            if counts[tmp[1]] == 0:
                del counts[tmp[1]]
            start += 1
        if tmp == '':
            print("done")
            break

    pass

def get_distinct(n, h):

    tmp = []
    distinct = []

    while (len(h) > 0):
        tmp.append(heapq.heappop(h))
        key = tmp[-1][1]
        if key not in distinct:
            distinct.append(key)
            if len(distinct) == n:
                break

    for t in tmp:
        heapq.heappush(h, t)

    return distinct

def getnextline(f):
    return f.readline()

if __name__ == '__main__':
    main()

                
