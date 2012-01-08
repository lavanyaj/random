import pickle
import sketch
import math
import numpy

tracefiledir='/n/fs/hhh/random/equinix-sanjose.dirA.20090416'
f = tracefiledir+'/130000-130000-5.raw.sketch'
input = open(f, 'rb')
s5 = pickle.load(input)
input.close()
f = tracefiledir+'/130000-130000-4.raw.sketch'
input = open(f, 'rb')
s4 = pickle.load(input)
input.close()
f = tracefiledir+'/130000-130000-3.raw.sketch'
input = open(f, 'rb')
s3 = pickle.load(input)
input.close()
f = tracefiledir+'/130000-130000-2.raw.sketch'
input = open(f, 'rb')
s2 = pickle.load(input)
input.close()
f = tracefiledir+'/130000-130000-1.raw.sketch'
input = open(f, 'rb')
s1 = pickle.load(input)
input.close()

print("cp of 2nd item . . . s2/s1 over first second: " + str(s2.F2()/s1.F2()))
print("cp of 3rd item . . . s3/s2 over first second: " + str(s3.F2()/s2.F2()))
print("cp of 4th item . . . s4/s3 over first second: " + str(s4.F2()/s3.F2()))
print("cp of 5th item . . . s5/s4 over first second: " + str(s5.F2()/s4.F2()))

print("2nd item out of 16 bits: " + str(-math.log(s2.F2()/s1.F2())))
print("3rd item out of 16 bits: " + str(-math.log(s3.F2()/s2.F2())))
print("4th item out of 16 bits: " + str(-math.log(s4.F2()/s3.F2())))
print("5th item out of 16 bits: " + str(-math.log(s5.F2()/s4.F2())))


#Over time:
s = []

for j in range(5):
	s.append(sketch.Sketch(j+1))

numseconds = 1
letters = ['a'+letter for letter in 'abcdefghijkl']
seconds = [str(num).zfill(2) for num in range(numseconds)]

subfiles = []
for s in seconds:
    subfiles.extend([(s, pair) for pair in letters])

arr = numpy.zeros((len(subfiles), len(s)))

time = -1
for s, pair in subfiles:
	time += 1
	for j in range(5):
		f = tracefiledir+'/1300'+s+'-1300'+s+'-'+str(j+1)+'.raw_'+pair+'.sketch'
		input = open(f, 'rb')
		s[j] = s[j] + pickle.load(input)
		input.close()
	#print("upto interval " + str(sub) + ": "),
	for j in [0,1,2,3]:
		sum_nijsqr = s[j+1].F2()
		sum_probijsqr = sum_nijsqr/s[j+1].numweights
		sum_nisqr = s[j].F2()
		sum_probisqr = sum_nisqr/s[j].numweights
		
		wtcondncp = sum_probijsqr/sum_probisqr
		H2 = -math.log(wtcondncp)
		arr[time, j+1] = H2
		#print(str(j+2)+ "th needs " + str(H2)),
	
print(arr)
	
