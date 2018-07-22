def factors(x):
	flist = []
	for i in range(1,x+1):
		if (x % i == 0):
			flist.append(i)
	return flist

def commonfactors(fm,fn):
	cf = []
	for i in fm:
		if i in fn:
			cf.append(i)
	return cf


def gcd(m,n):
	fm=factors(m)
	fn=factors(n)
	cf=commonfactors(fm,fn)
	return (cf[-1])

m=8
n=12
print(f"gcd{m,n} : ",gcd(m,n))
