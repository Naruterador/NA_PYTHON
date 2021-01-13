'''
输入2个整数，找出它们中的最大公约数与最小公倍数。
'''


#最大公约数函数
def maxDivider(a,b):
    c = a
    if b < a:
        c = b
    for d in range(c,0,-1):
        if a % d == 0 and b % d == 0:
            return d

#最小公倍数函数
def minMultiplier(a,b):
    c = a
    if b > a:
        c = b
    m = a * b
    for d in range(c,m + 1):
        if d % a == 0 and d % b == 0:
            return d


#主程序
a=input("a=")
b=input("b=")
a=int(a)
b=int(b)
print("最大公约数",maxDivider(a,b))
print("最小公倍数",minMultiplier(a,b))


