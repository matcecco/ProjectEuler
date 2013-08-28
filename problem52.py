import time

def srt(n):
	return sorted(str(n))

def check(x):
	X=[srt(x*i) for i in xrange(2,7)]
	if all([srt(x)==k for k in X]):
		return x

def solve():
	for i in xrange(1,10):
		x=10**i
		while len(str(x))==len(str(x*6)):
			if check(x):
				return x
			x=x+1
	return -1

if __name__ == '__main__':
	start_time = time.time()
	print('Result: {}'.format(solve()))
	elapsed_time = time.time() - start_time
	print('Elapsed time: {}'.format(elapsed_time))
