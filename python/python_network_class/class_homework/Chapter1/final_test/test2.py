'''
题目：判断101-200之间有多少个素数，并输出所有素数。
素数又被称为质数，是一个大于1的自然数，除了1和它自身外不能被其他自然数整除，否则就被称为合数
'''


h = 0
leap = 1

from math import sqrt


for m in range(0,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break

    if leap == 1 and m > 1:
        print ('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1

print ('The total is %d' % h)

