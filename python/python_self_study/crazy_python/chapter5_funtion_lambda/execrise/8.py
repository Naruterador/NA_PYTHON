#coding=utf-8
'''
定义一个fn(n)函数，该函数返回一个包含n个不重复的0~100之间整数的元组
(0,1,2,3,4,5,7,8,9,10)
(11,...............20)
....
(90,...............100)
'''


def fn(n):
    tul = []
    x = 1
    for i in range(int(100 / n)):
        tul.append([])
        for j in range(n):
            tul[i].append(x)
            x = x + 1
        tul[i] = tuple(tul[i])
    return tuple(tul)

print(fn(5))
