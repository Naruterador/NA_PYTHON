#coding=utf-8
'''
定义一个fn(n)函数，返回n的阶乘
'''

def fn(n):
    k = 1
    for i in range(1,n + 1):
        k = k * i
    return k

def fn1(n):
    if n == 1:
        return 1
    else:
        return n * fn(n - 1)


result = fn1(3)
print(result)