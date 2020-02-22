'''
哥德巴赫猜想:任何一个6以上的偶数都可以分解为两个素数的和
例如 6 = 3 + 3   8 = 5 + 3 10 = 5 + 5
'''
while True:
    n = input("输入6以上的偶数:")
    n = int(n)
    if n % 2 == 0 and n >= 6:
        break
        
#p的最大值maxp
maxp = n // 2
p = 1
while p <= maxp:
    #判断p是否是素数，flag=True表示是素数
    flag = True
    for k in range(2,p):
        if p % k == 0:
            #p可以被比它小的整数除尽，不是素数
            flag = False
            break
    #如果p是素数，再次判断q是否时素数
    if flag:
        q = n - p
        for k in range(2,q):
            if q % k == 0:
                # q可以被比它小的整数除尽，不是素数
                flag = False
                break
        #q也是素数，得到一个分解n=p+q
        if flag:
            print(n,"=",p,"+",q)
    p = p + 2
print("done!")
