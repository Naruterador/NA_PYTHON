#coding=utf-8
'''
装饰器2
'''

def foo(fn):
    def bar(*args):
        print(args)
        #print("===1===",args)
        #n = args[0]
        #print("===2===",n * (n - 1))
        #print(fn.__name__)
        #fn(n * (n - 1))
        #print("+" * 15)
        #return fn(n * (n - 1))
    return bar

@foo
def my_test(a):
    print("===my_test函数==",a)

print(my_test)       #用于打印查看函数的调用，这里发现调用的其实是bar函数
my_test(10)
#my_test(5,6)
