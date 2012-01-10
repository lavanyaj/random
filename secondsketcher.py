import sketch
import sys
import os
import pickle
import myhash

def main():
    f = open(sys.argv[2])
    T = int(sys.argv[1])
    s = []
    mh = myhash.MyHash()
    for i in range(T):
        s.append(sketch.Sketch(i+1))

    i = 0
    while True:
        i += 1
        if (i%100000 == 0):
            print(str(i) + "lines done")
        line = f.readline()
        if line == '':
            break
        words = line.rstrip().split()
        blocks = [int(w) for w in words]
        
        for i in range(T):
            Si = mh.changeVec16toU64(blocks[:i+1])
            s[i].insert(Si, 1)
        
    print("main sketch's numweights, sumweights, fi, F2")

    

    print(str(s[0].numweights) + ","
          + str(s[0].sumweights) + ","
          + str(12) + ": " + str(s[0].fi(12)) + ","
          + str(s[0].F2()))
    print("---")

    for i in range(T):
        output=open(sys.argv[2]+'.sketch.'+str(i+1), 'wb')
        pickle.dump(s[i], output)
        output.close()
        
if __name__ == '__main__':
    main()
   
