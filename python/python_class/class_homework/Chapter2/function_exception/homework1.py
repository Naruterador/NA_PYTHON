
'''
函数f打印出1,2,3的6个排列，空缺语句是
'''

def f(n):
	for a in range(1,n):
		for b in range(1,n):
			for c in range(1,n):
				if a != b and b != c and c != a:
					print(a,b,c)

f(4)