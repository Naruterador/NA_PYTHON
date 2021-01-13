#coding=utf-8
'''
定义一个fn(n)函数，该函数返回1~n的立方和，即求1+2*2*2+3*3*3+...+n*n*n
'''


def fn(n):
    k = 0
    for i in range(1,n + 1):
        k = k + (i*i*i)
    return k

result = fn(3)
print(result)