import random
import sys
import os


class MyHash:

    def __init__(self):
        self.H61_4 = []
            
        self.PRIME61 = (1L << 61) - 1
        self.H61_2 = self.H61_4
        self.TWOEXP32 = 1L << 32


        # used by sketch
        # table i can choose ith hash function
        self.H89_4 = [
(1772827544918689723711488L, 229182717010700717244022784L, 61335081999261809770496000L, 242397189984972585144680448L),
(150907518729425991961149440L, 275651920258584919997939712L, 267056995618925732975083520L, 246769574788510212153147392L),
(167058519399355607649615872L, 278066062643717901031309312L, 145751155655736680410775552L, 227642893928028405711765504L),
(111245242850277273597116416L, 256550441219369059613671424L, 181341927198451199387893760L, 132566685744653801376186368L), 
(112294571144379747461496832L, 227486171485606271634112512L, 303782877842458985938026496L, 176809507987317256282439680L),
(217648414279586970530217984L, 242891929018275040835141632L, 156503241943022024244854784L, 209081351184955351815421952L),
(47079408087840314491928576L, 89252097077795126840918016L, 239449191583989389047365632L, 43065283183772366534606848L),
(141280161482226621002809344L, 7982655365064675351855104L, 167786168178049074398756864L, 150993326327966898010980352L),
(20953592306286876398977024L, 177514909463624717231456256L, 54244687129253165171474432L, 257358465021757930636050432L)
           ]
        # used by long vector to 64 bit key-izer
        self.H89_2 = [
            (171987314105482373079498752L, 36152823489033712462462976L),
(263304600142228490154934272L, 294566867087490231813799936L),
(39970048219593223402684416L, 250627012837541938678726656L),
(189025000674173858443427840L, 56248416389781773048872960L),
(262059299953243417311444992L, 243307157614488738668216320L),
(11309759173708883181961216L, 118548192608562169763594240L),
(221420369889408796195815424L, 191265466874726829457932288L),
(303993004848293129224192000L, 262910061429782847342772224L),
(39858193546498506972200960L, 177195037750751023016706048L),
(26178804732191692931727360L, 47317428722693217147944960L),
(305516036532909418488004608L, 98312794704823872387022848L),
(192957671866596866727608320L, 175622365974673792111214592L)]
        self.PRIME89 = (1L << 89) - 1
        self.TWOEXP64 = 1L << 64


# vector to key-izer all versions use the same constants
    def changeVec16toU64(self, vector):
        """ if vector has more than four 16 bit items, 2-univ. hash 
        otherwise just add them up """

        if len(vector) < 5:
            return self.four16toU64(vector)
        else:
            Vec64 = self.Vec16toVec64(vector)
            start = self.CW89hash2_U64(Vec64[0], self.TWOEXP64, self.H89_2[0])
            for i in range(1, len(Vec64)):
                start = start ^ self.CW89hash2_U64(Vec64[i], self.TWOEXP64, self.H89_2[i])
            return start


    def four16toU64(self, vector):
        length = min(len(vector), 4)
        return sum([vector[i] * (2**16)**(length-1-i) for i in range(length)])

    def Vec16toVec64(self, vector):
        length = len(vector)
        return [self.four16toU64(vector[i:i+4]) for i in range(0, length, 4)]

    def CW61hash2_U32(self, x, M, h61_2):
        """ 2 Universal Hashing for x, M < PRIME61-1"""

#(ax+b mod p) mod m where a, b randomly from 0 through p-1 a not 0, p > m"""        
        ax = h61_2[0]*x
        b = h61_2[1] 
        k = (ax + b) % self.PRIME61
        return k % M

    def CW61hash4_U32(self, x, M, h61_4):
        """ 4 Universal Hashing for x, M < PRIME61-1"""
#(ax+b mod p) mod m where a, b randomly from 0 through p-1 a not 0, p > m"""        
        ax3 = h61_4[0]*(x**3)
        bx2 = h61_4[1]*(x**2)
        cx = h61_4[2]*(x)
        d = h61_4[3]

        k = (ax3 + bx2 + cx + d) % self.PRIME61
        return k % M

    # Hopefully python optimizes when it sees 11111.... 

    def CW89hash2_U64(self, x, M, h89_2):
        """ 2 Universal Hashing for x, M < PRIME89-1"""
#        """ 2-Universal Hashing needs AX^3 + BX^2 + ... mod p"""
        ax = h89_2[0]*(x)
        b = h89_2[1]*(x)
        k = (ax + b) % self.PRIME89
        return k % M

    def CW89hash4_U64(self, x, M, h89_4):
        """ 4 Universal Hashing for x, M < PRIME89-1"""
#        """ 4-Universal Hashing needs AX^3 + BX^2 + ... mod p"""
        ax3 = h89_4[0]*(x**3)
        bx2 = h89_4[1]*(x**2)
        cx = h89_4[2]*(x)
        d = h89_4[3]
        k = (ax3 + bx2 + cx + d) % self.PRIME89
        return k % M
    
    
