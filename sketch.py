import copy
import sys
import os
import myhash
import numpy

class Sketch:
    def __init__(self, n):
        self.TWOEXP9 = 1 << 9
        # Count-Sketch error in F2 is sqrt(2/m) of F2 -- 1/16 of F2
        # CM error in fi is e/m of N -- 1/20 of N
        self.height = 3
        self.width = self.TWOEXP15
        self.datadim = n
        self.numweights = 0
        self.sumweights = 0
        self.mh = myhash.MyHash()

        self.C = numpy.zeros((self.height, self.width), dtype=int)#[]
        #for i in range(self.height):
        #    tmp = [0]*self.width
        #    self.C.append(tmp)

    def insert(self, x64, weight):
        for i in range(self.height):
            hashi = self.mh.CW89hash4_U64(x64, self.width, self.mh.H89_4[i])
            self.C[i,hashi] += weight
        self.numweights += 1
        self.sumweights += weight

    def fi(self, x64):
        fi = numpy.zeroes(self.height)
        for i in range(self.height):
            hashi = self.mh.CW89hash4_U64(x64, self.width, self.mh.H89_4[i])
            Ci = self.C[i,hashi] 
            #other = hashi + (-1)**(hashi%2) # bored
            #Cother = self.C[i,other]
            fi[i] = Ci #- Cother

        return min(fi)

    def F2(self):
        F2 = numpy.zeros(self.height)
        for i in range(self.height):
            for j in range(self.width/2 - 1):
                F2[i] += (self.C[i,2*j] - self.C[i,2*j+1])**2
        return numpy.mean(F2)


    def __add__(self, other):
        if not self.compatible(other):
            return NotImplemented

        sumsketch = copy.deepcopy(self)
        sumsketch.C += other.C
        
        sumsketch.numweights += other.numweights
        sumsketch.sumweights += other.sumweights
        # that's why you add only if they're unweighted

        return sumsketch

    
    def compatible(self, other):
        return (self.height == other.height 
                and self.width == other.width
                and self.datadim == other.datadim
#                and self.sumweights == self.numweights
 #               and other.sumweights == other.numweights
                )
