import sketch
import sys
import os
import pickle

def main():
    """ USAGE: combinesketches 2 130000-130000-3.raw.sketch 130000-130000-2.raw_ab 130000-"""
    sketchfiles = sys.argv[3:]

    s = sketch.Sketch(int(sys.argv[1]))
    for f in sketchfiles:
        input = open(f, 'rb')
        s = s + pickle.load(input)
        input.close()

    
    output = open(sys.argv[2], 'wb')
    pickle.dump(s, output)
    output.close()

    print("main sketch's numweights, sumweights, fi, F2")
    print(str(s.numweights) + ","
          + str(s.sumweights) + ","
          + str(12) + ": " + str(s.fi(12)) + ","
          + str(s.F2()))
    print("---")

if __name__ == '__main__':
    main()
   
