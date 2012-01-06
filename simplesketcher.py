import sketch
import sys
import os
import pickle

def main():
    f = open(sys.argv[2])
    s = sketch.Sketch(int(sys.argv[1]))
    i = 0
    while True:
        i += 1
        if (i%100000 == 0):
            print(str(i) + "lines done")
        line = f.readline()
        if line == '':
            break
        s.insert(int(line.rstrip().split(',')[1]), 1)
        
    print("main sketch's numweights, sumweights, fi, F2")
    print(str(s.numweights) + ","
          + str(s.sumweights) + ","
          + str(12) + ": " + str(s.fi(12)) + ","
          + str(s.F2()))
    print("---")
    output=open(sys.argv[2]+'.sketch', 'wb')
    pickle.dump(s, output)
    output.close()
if __name__ == '__main__':
    main()
   
