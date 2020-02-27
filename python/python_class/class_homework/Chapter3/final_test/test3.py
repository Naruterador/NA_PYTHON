
def f(st):
	i = 0
	while i < len(st):
		if st[i] % 2 == 0:
			del st[i]
		else:
			i += 1

st = [1,2,3,4,5,6]
f(st)
print(st)