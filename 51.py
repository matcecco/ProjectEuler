import math
import time
from itertools import combinations

def is_prime(x):
	if x==2:
		return True
	if x%2==0 or x<2:
		return False
	sq=int(math.sqrt(x))
	for i in xrange(3,sq+1,2):
		if x%i==0:
			return False
	return True

def serie(s,z,n):
	ret=[s]
	for x in xrange(n+1,10):	
		sc=list(s)
		for w in z:
			sc[w]=str(x)
		if is_prime(int("".join(sc))):
			ret.append("".join(sc))
	return ret

def test(s,i): #s=number(in letter),i=index to test
	c=s.count(s[i])
	n=int(s[i])
	for k in xrange(1,c+1): #comb c,k
		comb_pk=combinations([j for j in xrange(0,len(s)) if s[j]==s[i]], k)

		for comb in comb_pk:
			nprimes=1
			for x in xrange(n+1,10):	#replace n with x
				tmpstr=list(s) #copy string number into a list
				for w in comb:
					tmpstr[w]=str(x) #replace occurrence
				if is_prime(int("".join(tmpstr))):
					nprimes=nprimes+1
					if nprimes>7: #found
						print s,serie(s,comb,n)
						return True
				if x-nprimes>1:
					break
	return False

def problem51():
	for i in xrange(1,1000000,2): 
		if is_prime(i):
			s=str(i)
			z=[0,0,0]
			for k in xrange(len(s)):
				if z[0]==0 and s[k]=='0':
					if test(s,k):
						return 1
					z[0]=1
				elif z[1]==0 and s[k]=='1':
					if test(s,k):
						return 1
					z[1]=1
				elif z[2]==0 and s[k]=='2':
					if test(s,k):
						return 1
					z[2]=1
	return 0

if __name__ == '__main__':
	start = int(round(time.time() * 1000))
	problem51()
	print 'completed in', int(round(time.time() * 1000))-start,'ms'
