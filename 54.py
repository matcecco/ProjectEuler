values = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}

def find_equals(p):
	ret=0
	mod=0
	for i in range(13):
		n=0
		for k in p.keys():
			if p[k][i]==1:
				n=n+1
		if n==2:				#punti per coppia min(1015) max(1195)
			if ret>2: #full	
				ret=ret+7		#add 7k bonus per full min(12230) max(18030)
			ret=ret+1
			mod=mod+15*(i+1)
		elif n==3:				#punti per tris min(4200) max(10000)
			if ret>2: #full
				ret=ret+7		#add 7k bonus per full min(12230) max(18030)
			ret=ret+4
			mod=mod+400*(i+1)
		elif n==4:				#punti per poker min(19015) max(19195)
			ret=ret+19
			mod=mod+15*i
	return ret*1000+mod

def find_color(p):				#punti colore 12000
	ret=0
	n=0
	for k in p.keys():
		for i in range(13):
			if p[k][i]==1:
				n=n+1
		if n==5:
			return 12000
	return 0

def find_scala(p):				#punti scala 11000 (-10 se parte dall asso basso)
	ret=0
	n=[0]*13

	for i in range(13):
		for k in p.keys():
			if p[k][i]==1:
				n[i]=1
				break
	count=0
	if n[12]==1:
		count=1
	for i in n:
		if i==1:
			count=count+1
		else:
			count=0
		if count==5:
			return 11000 -n[0]*10
	return 0

def evaluate(p):
	ret = 0
	ret=ret+find_equals(p) 
	ret=ret+find_scala(p) 
	ret=ret+find_color(p) 
	return ret

def check(p1,p2):
	r1=0 #carta alta
	r2=0 #carta alta
	p1S = {'H':[0]*13,'C':[0]*13,'D':[0]*13,'S':[0]*13}
	p2S = {'H':[0]*13,'C':[0]*13,'D':[0]*13,'S':[0]*13}
	for i in p1:
		p1S[i[1]][values[i[0]]]=p1S[i[1]][values[i[0]]]+1
		if r1<values[i[0]]:
			r1=values[i[0]]
	for i in p2:
		p2S[i[1]][values[i[0]]]=p2S[i[1]][values[i[0]]]+1
		if r2<values[i[0]]:
			r2=values[i[0]]
	
	return r1+evaluate(p1S),r2+evaluate(p2S)

if __name__ == '__main__':
	in_file = open("pokertest.txt")
	win=0
	for line in in_file:
		s=line.split(' ')
		a,b=check(s[:5],s[5:])
		if a>b:
			win=win+1
	in_file.close()
	print win
	raw_input()
