'''
1、案例描述
我们已经编写过MyDate的日期类，再增加时分秒的数据，派生出日期时间类MyDateTime。
 
2、案例分析
class MyDate:
    def __init__(self,y,m,d):
    ......

class MyDateTime(MyDate):
    def __init__(self,y,mo,d,h,mi,s):
    ......
'''


class MyDate:
    __months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, y, m, d):
        if y < 0:
            raise Exception("无效年份")
        if m < 1 or m > 12:
            raise Exception("无效月份")
        if y % 40 == 0 or y % 4 == 0 and y % 100 != 0:
            MyDate.__months[2] = 29
        else:
            MyDate.__months[2] = 28
        if d < 1 or d > MyDate.__months[m]:
            raise Exception("无效日期")
        self.year = y
        self.month = m
        self.day = d

    def show(self, end='\n'):
        print("%04d-%02d-%02d" % (self.year, self.month, self.day), end=end)


class MyDateTime(MyDate):
    def __init__(self, y, m, d, h, mi, s):
        MyDate.__init__(self, y, m, d)
        if h < 0 or h > 23 or mi < 0 or mi > 59 or s < 0 or s > 59:
            raise Exception("无效时间")
        self.hour = h
        self.minute = mi
        self.second = s

    def show(self):
        MyDate.show(self, end=" ")
        print("%02d:%02d:%02d" % (self.hour, self.minute, self.second))


try:
    d = MyDateTime(2017, 7, 8, 23, 12, 34)
    d.show()
except Exception as e:
    print(e)
