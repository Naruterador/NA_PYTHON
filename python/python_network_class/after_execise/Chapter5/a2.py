#定义一个计算机类MyComputer，它包含CPU类型(String类型）、RAM内存大小(Integer类型)、HD硬盘大小(Integer类型)，设计它的构造函数，并设计一个显示函数，建立一个MyComputer对象并调用该显示函数显示。

class MyComputer(object):
    
    def __init__(self,CPU_type,RAM_size,HD_size):
        self.CPU_type = CPU_type
        self.RAM_size = RAM_size
        self.HD_size = HD_size
    
    def getsize(self):
        s1 = "CPU类型为:" + self.CPU_type
        s2 = "RAM内存大小为:" + str(self.RAM_size) + "GB"
        s3 = "硬盘大小为:" + str(self.HD_size) + "GB"
        output = s1 + "\n" + s2 + "\n" + s3
        return output
    
    def setsize(self,dict_com):
        
        self.CPU_type = dict_com["CPU_type"]
        self.RAM_size = dict_com["RAM_size"]
        self.HD_size = dict_com["HD_size"]
    
    def delsize(self):
        self.CPU_type = ""
        self.RAM_size = 0
        self.HD_size = 0

    size = property(getsize,setsize,delsize)

mc = MyComputer("I3 6100",16,500)

print(mc.size)
mc.size = {"CPU_type":"I5 7500","RAM_size":32,"HD_size":1000}
print("--------------------------------------------------------------")
print(mc.size)