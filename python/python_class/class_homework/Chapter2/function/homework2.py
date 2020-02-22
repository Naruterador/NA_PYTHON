x = 0
y = 1

def fun(a,b):
	global x,y
	x = b
	y = a

fun(x,y)
print(x,y)