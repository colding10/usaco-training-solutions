'''
ID: colindi1
LANG: PYTHON3
TASK: milk2
'''

#import os
#try:
#    os.chdir(os.path.dirname(__file__))
#except:
#    pass

def sortKeyGen(line):
	if line:
		start, end = map(int, line.strip().split(" "))
		return start

with open('milk2.in','r') as file:
	nCows = int(file.readline().strip())
	times = file.read().split('\n')

times = list(filter(None, times))
times.sort(key = sortKeyGen)
mStart, mEnd = map(int,times[0].strip().split(" "))

longestC = mEnd-mStart
longestI = 0

for time in times:
	if time:
		start, end = map(int,time.strip().split(" "))

		if start-mEnd >= longestI :
			longestI = start-mEnd

		if mStart<=start and start<=mEnd:
			if mEnd<end:
					mEnd=end
		else:
			if mEnd-mStart > longestC:
					longestC = mEnd-mStart
			mStart,mEnd = start,end

with open('milk2.out','w') as file:
	file.write(f"{longestC} {longestI}\n")