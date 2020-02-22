x = 0
y = 1

def fun(x,y):
	t = x
	x = y
	y = t

fun(x,y)
print(x,y)