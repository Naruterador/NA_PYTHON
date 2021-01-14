#coding=utf-8
'''
定义一个函数，该函数可接受一个list作为参数，该函数使用冒泡排序对list排序
冒泡排序思想：
冒泡排序就是每趟排序过程中通过两两比较，找到第i个小（大）的元素，将其往上排。
'''

class bubblesort(object):
    def __init__(self,lista):
        self.lista = lista

    def __bubblesortf(self):
        x = 0
        for i in range(len(self.lista)):
            k = 0
            for j in range(1,len(self.lista)):
                if self.lista[k] > self.lista[j]:
                    x = self.lista[k]
                    self.lista[k] = self.lista[j]
                    self.lista[j] = x
                k = k + 1

        return self.lista

    def printout(self):
        print(self.__bubblesortf())

lista = [4,3,1,2,5,10]
b1 = bubblesort(lista)
b1.printout()

