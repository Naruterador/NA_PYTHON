#设计一个整数类MyInteger，它有一个整数变量，并有一个Value属性
#可以通过为Value存取该变量的值，还有一个转二进制字符串的成员函数toBin及转十六进制字符串的成员函数toHex



class MyInter(object):

    def __init__(self,Value):
        self.value = Value
    

    def toBin(self):
        value_b = self.value 
        binarylist = []
        i = 0
        while value_b >= 1:
            i = value_b % 2
            value_b //= 2
            binarylist.append(i)

        binarylist.reverse()
        s = "b"
        for j in binarylist:
            s += str(j)
        
        return s

    def toHex(self):
        value_h = self.value
        hexbinary = []
        i = 0
        while True:
            i = value_h % 16
            value_h //= 16
            hexbinary.append(i)
            if value_h == 0:
                break
        hexbinary.reverse()
        
        s = "0x"
        for i in hexbinary:
            if i == 10:
                s += 'A'
            elif i == 11:
                s += 'B'
            elif i == 12:
                s += 'C'
            elif i == 13:
                s += 'D'
            elif i == 14:
                s += 'E'
            elif i == 15:
                s += 'F'
            else:
                s += str(i)
        return s
        

mi = MyInter(255)
print(mi.toBin())
print(mi.toHex())