#coding = utf-8
'''
定义一个函数，该函数可接受一个list作为参数，该函数使用直接选择排序对list排序
选择排序的基本思想：
首先在末尾排序的数列中找到最小或最大的元素，然后将其放到数列的启始位置；接着，再从剩余未排序的元素中寻找最小或最大的元素，然后放到
已排序序列的末尾，一次类推，直到所有元素均排序完毕。
'''

class selectsort(object):
    def __init__(self,sortlist):
        self.sortlist = sortlist

    def __sort(self):
        k = 0
        for i in range(len(self.sortlist)):
            for j in range(i + 1,len(self.sortlist)):
                if self.sortlist[i] > self.sortlist[j]:
                    k = self.sortlist[i]
                    self.sortlist[i] = self.sortlist[j]
                    self.sortlist[j] = k
                else:
                    pass
        return self.sortlist


    def printout(self):
        print(self.__sort())

lista = [9,1,2,5,7,4,8,6,5,3]
ss1 = selectsort(lista)
ss1.printout()

