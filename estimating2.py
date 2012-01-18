import sys
import pickle
import sketch
import math
import numpy

def main():
	numpy.set_printoptions(precision=3)

	"USAGE: python2.6 estimating2.py 1 6 for first 1 second from 06"
	if len(sys.argv) < 2:
		print(main.__docstring__)
		return
	start = 5
	rawfiledir='/n/fs/hhh/random/raw'
	T = 10
#Over time:
        s = []

	for j in range(T):
		s.append(sketch.Sketch(j+1))

	numseconds = int(sys.argv[1])
	letters = ['a'+letter for letter in 'abcdefg']
	seconds = [str(num).zfill(2) for num in range(start, start+1+numseconds)]

	subfiles = []
	for sec in seconds:
		subfiles.extend([(sec, pair) for pair in letters])

	arr = numpy.zeros((len(subfiles), len(s)))

	time = -1

	for sec, pair in subfiles:
		time += 1
		for j in range(T):
			#dp-130900-130900-T10.raw_ag.sketch.1
			f = rawfiledir+'/dp-13'+sec+'00-13'+sec+'00-T10.raw_'+pair+'.sketch.'+str(j+1)
			try:
				input = open(f, 'rb')
			except IOError:
#				print("could not open " + str((sec,pair)) + " file " + f)
				continue
			s[j] = s[j] + pickle.load(input)
			input.close()
	#print("upto interval " + str(sub) + ": "),
	        for j in range(T-1):
			if (s[j+1].numweights != s[j+1].numweights):
				print("weights not equal")
			sum_nijsqr = s[j+1].F2()
			sum_probijsqr = sum_nijsqr
			sum_nisqr = s[j].F2()
			sum_probisqr = sum_nisqr
		
			wtcondncp = sum_probijsqr/sum_probisqr
			H2 = -math.log(wtcondncp, 2)
			if (sys.argv[2]=='h'):
				arr[time, j+1] = H2
			else:
				arr[time, j+1] = sum_nijsqr
		#print(str(j+2)+ "th needs " + str(H2)),

	rows, columns = arr.shape

	for c in range(columns):
		print("S"+str(c+1)+' '),#+"/S"+str(c)+' '),
	print('')
	
	for r in range(rows):
		for c in range(columns):
			print('%.3f ' % arr[r, c]),
		print('')

		
#	print(arr)
	output = open('e2out', 'wb')
	pickle.dump(arr, output)
	output.close()
	pass

if __name__ == '__main__':
	    main()
