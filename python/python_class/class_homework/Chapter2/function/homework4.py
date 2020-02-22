x = 0
y = 1

def fun(a,y):
	global x
	t = x
	x = y
	y = t

fun(x,y)
print(x,y)