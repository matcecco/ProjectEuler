def is_palindrome(str):
	l=len(str)
	for i in range(0,l/2):
		if str[i]!=str[l-i-1]:
			return False
	return True

def is_lychrel(n,loop=0):
	if loop==50:
		return 1
	sn=n+int(str(n)[::-1])
	#print '\t',loop+1,n,'+',str(n)[::-1],'=',sn
	if is_palindrome(str(sn)):
		#print '\t',sn,'is palindrome'
		return 0
	return is_lychrel(sn,loop+1)

if __name__ == '__main__':
	ret=0
	for i in range(1,10000):
		#print 'testing',i
		ret=ret+is_lychrel(i)
	print ret
	raw_input()
