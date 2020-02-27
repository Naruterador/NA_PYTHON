####函数的接收方式

1.元组可变参数的函数

def fun(x,y,*args):
    print(x,y)
    print(args)

fun(1,2)
fun(1,2,3)
fun(1,2,3,4)

结果：
1 2
()
1 2
(3,)


2.元组参数收集的逆向过程

def add(x,y):
	return x + y

params = (1,2)

print(add(*params))

结果是:
3




3.字典可变参数的函数
def fun(x,y=2,**kargs):
    print(x,y)
    print(kargs)

fun(1,2)
fun(1,2,z=3)
fun(1,2,a=3,b="demo")
fun(x=1,y=2,z=3)
fun(y=1,x=2,z=5,s="demo")
fun(x=1,z=3)

结果：
1 2
{}
1 2
{'z': 3}
1 2
{'a': 3, 'b': 'demo'}
1 2
{'z': 3}
2 1
{'z': 5, 's': 'demo'}
1 2
{'z': 3}


4.字典参数的逆向接收过程

def with_starts(**kwds):
	print(kwds['name'] + 'is' + kwds['age'] + 'year old' )


def without_starts(kwds):
	print(kwds['name'] + 'is' + kwds['age'] + 'year old' )

kwds = {'name':'king','age': '33'}

with_starts(**kwds)
without_starts(kwds)

结果:
kingis33year old
kingis33year old