'''
建立一个时间类Time，它包含时hour, 分minute，秒second的实例属性
(1) 设计时间显示函数show(self)；
(2) 设计两个时间大小比较函数compare(self, t)，其中t是另外一个时间；
'''


class Time(object):
    
    def __init__(self,hour,minute,second):
        self.timelist = []
        if hour >= 0 and hour <= 23:
            self.h = hour
        else:
            raise ValueError("Set hour between 0 - 23!")
        
        if minute >= 0 and minute <= 59:
            self.m = minute
        else:
            raise ValueError("Set minute between 0 - 59")

        if second >= 0 and second <= 59:
            self.s = second
        else:
            raise ValueError("Set seond between 0 - 59")
        
        self.timelist.append(self.h)
        self.timelist.append(self.m)
        self.timelist.append(self.s)


    def show(self):
        print("Time is: %d:%d:%d" %(self.h,self.m,self.s))

    def compare(self,t):
        if self.h > t.h:
            return True
        elif self.m > t.m:
            return True
        elif self.s > t.s:
            return True
        else:
            return False

t = Time(22,55,13)
t1 = Time(11,52,58)

if t.compare(t1):
    print("t时间大")
else:
    print("t1时间大")
