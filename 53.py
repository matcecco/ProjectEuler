if __name__ == '__main__':
	res=0
	fact=[1]
	for i in xrange(1,101):
		fact.append(fact[i-1]*i)
		for j in xrange(1,i):
			k=fact[i]/(fact[j]*fact[i-j])
			if k>1000000:
				res=res+1
	print res
	