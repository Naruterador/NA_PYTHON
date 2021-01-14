#coding=utf-8
'''
定义一个fn(n)函数，其中n表示输入n行n列矩阵(数的方阵)。在输出时，先输出n行n列的矩阵，在输出该矩阵的转置形式。
例如输出3的时候先输出
1 2 3
4 5 6
7 8 9

在输出


1 4 7
2 5 8
3 6 9
'''


class Chmartix(object):

    def __init__(self,n):
        self.n = n

    def __printmar(self):
        x = 1
        lista = []
        for i in range(self.n):
            lista.append([])
            for j in range(self.n):
                lista[i].append(x)
                x = x + 1
        return lista

    def __chmar(self):
        x = 0
        lista = []
        for i in range(self.n):
            x = i + 1
            lista.append([])
            for j in range(self.n):
                lista[i].append(x)
                x = x + self.n
        return lista



    def printout(self):
        for i in self.__chmar():
            print(i)




m1 = Chmartix(4)
m1.printout()


