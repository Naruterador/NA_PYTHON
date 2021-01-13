'''
1、案例描述
设计一个通用的最大值函数max，它可以计算出任意个数的最大值。
 
2、案例分析
函数设计成带任意参数*args的形式：
def max(*args)
那么就可以带任意参数调用了，例如：
print(max(1,2))
print(max(1,2,3,4))
'''

def max(*args):
    a = args[0]
    for i in args:
        if i > a:
            a = i
    print(a)


