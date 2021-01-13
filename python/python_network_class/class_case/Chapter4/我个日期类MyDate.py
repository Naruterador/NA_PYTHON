'''
1、案例描述
编写一个日期类MyDate，拥有年月日的数据。
 
2、案例分析
定义MyDate__init__函数实现对象的初始化，在数据不合理时抛出异常。
'''

class MyDate:
    __months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        if y < 0:
            raise Exception("无效年份")
        if m < 1 or m > 12:
            raise Exception("无效月份")
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            MyDate.__months[2] = 29
        else:
            MyDate.__months[2] = 28
        if d < 1 or d > MyDate.__months[m]:
            raise Exception("无效日期")
        self.year = y
        self.month = m
        self.day = d

    def show(self, end='\n'):
        print("%04d-%02d-%02d" % (self.year, self.month, self.day))

try:
    d = MyDate(2017, 7, 8)
    d.show()
except Exception as e:
    print(e)
