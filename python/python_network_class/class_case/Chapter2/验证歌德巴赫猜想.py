def IsPrime(m):
	for n in range(2,m):
		if m % n == 0:
			return 0
		return 1
		
for n in range(6,101,2):
	for p in range(3,n + 1,2):
		q = n - p
		if IsPrime(p) and IsPrime(q):
			print(n,"=",p,"+",q)
			break
