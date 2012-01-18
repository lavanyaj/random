
import sys
import os
import heapq
from myhash import *


def main():
    """ USAGE: e.g., python2.7 distinctNvectors.py 3 <test.txt """
    MyH = MyHash()
    if (len(sys.argv) < 2):
        print main.__doc__
        return
    N = int(sys.argv[1])
    h = []
    f = sys.stdin #open(sys.argv[2], 'r')
    counts = {}

    start = 0
    lastreadline = -1


#    string = '0abcdefghi'
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
#            print(string[port] + ' read')
            
            if port in counts:
                counts[port] += 1
            else:
                counts[port] = 1

            heapq.heappush(h, (lastreadline, port))
        
        else:
#            print("counts now has N so get distinct")
            distinctvector = get_distinct(N, h)
            
            for p in distinctvector:
                print(p),
            print('')

            # since you didn't mention q or q+1 h.f.
            # uses first q of H89_64 for Sn in all prog.
            # etc.
#            if N == 1:
#                Sn_u64 = 0
#            else:
#                Sn_u64 = MyH.changeVec16toU64(distinctvector[:-1])

#            Xnplus1_u64 = MyH.changeVec16toU64(distinctvector)
#            prinstr(Sn_u64) + ',' + str(Xnplus1_u64))
#            print("popping last read item")
            tmp = heapq.heappop(h)
            #print(tmp)
            counts[tmp[1]] -= 1
            if counts[tmp[1]] == 0:
                del counts[tmp[1]]
            start += 1
#            print("now tracking distinct items starting from line " + str(start))
        if tmp == '':
#            print("done")
            break

    pass

def get_distinct(n, h):

    tmp = []
    distinct = []
#    print("popping from heap in order last read")
    while (len(h) > 0):
        tmp.append(heapq.heappop(h))
        key = tmp[-1][1]
#        print(str(tmp[-1]) + " keyed by " + str(key))

        if key not in distinct:
#            print("new key")
            distinct.append(key)
            if len(distinct) == n:
#                print("have popped first n distinct keys")
                break
#    print("putting everything back on heap")
    for t in tmp:
        heapq.heappush(h, t)
#    print("heap now has" + str(len(h)))
    return distinct

def getnextline(f):
    return f.readline()

if __name__ == '__main__':
    main()

                
