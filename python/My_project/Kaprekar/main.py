class Kaprekar(object):

    def __init__(self):
        self.num = 0

    def __threeDigit(self,num):
        num1 = 0
        num2 = 0
        for i in range(1000):
            #获取当前三位数的个位、十位、和百位
            newnumlist = []
            hundreds = num % 1000 // 100
            decade = num % 100 // 10
            the_unit = num % 10
            newnumlist.append(hundreds)
            newnumlist.append(decade)
            newnumlist.append(the_unit)

            Alist = sorted(newnumlist,reverse=True)
            num1 = Alist[0] * 100 + Alist[1] * 10 + Alist[2]
            Blist = sorted(newnumlist)
            num2 = Blist[0] * 100 + Blist[1] * 10 + Blist[2]
            
            num = num1 - num2
        print(num)

    def __fourDigit(self,num):
        num1 = 0
        num2 = 0
        for i in range(1000):
            #获取当前四位数的个位、十位、百位和千位
            newnumlist = []
            kilobit = num % 10000 // 1000
            hundreds = num % 1000 // 100
            decade = num % 100 // 10
            the_unit = num % 10

            newnumlist.append(kilobit)
            newnumlist.append(hundreds)
            newnumlist.append(decade)
            newnumlist.append(the_unit)

            Alist = sorted(newnumlist,reverse=True)
            num1 = Alist[0] * 1000 + Alist[1] * 100 + Alist[2] * 10 + Alist[3]
            Blist = sorted(newnumlist)
            num2 = Blist[0] * 1000 + Blist[1] * 100 + Blist[2] * 10 + Blist[3]
            
            num = num1 - num2
            
        print(num)

    def __fiveDigit(self,num):
        num1 = 0
        num2 = 0
        for i in range(1000):
            #获取当前五位数的个位、十位、、百位、千位和万位
            newnumlist = []
            myriabit = num // 10000
            kilobit = num % 10000 // 1000
            hundreds = num % 1000 // 100
            decade = num % 100 // 10
            the_unit = num % 10

            newnumlist.append(myriabit)
            newnumlist.append(kilobit)
            newnumlist.append(hundreds)
            newnumlist.append(decade)
            newnumlist.append(the_unit)

            Alist = sorted(newnumlist,reverse=True)
            num1 = Alist[0] * 10000 + Alist[1] * 1000 + Alist[2] * 100 + Alist[3] * 10 + Alist[4]
            Blist = sorted(newnumlist)
            num2 = Blist[0] * 10000 + Blist[1] * 1000 + Blist[2] * 100 + Blist[3] * 10 + Blist[4]
            
            num = num1 - num2
        print(num)


    def __checknumlenth(self,num):
        if len(str(num)) >= 3 and len(str(num)) <= 5:
            return True
        else:
            return False

    def run(self,num):
        if self.__checknumlenth(num):
            if len(str(num)) == 3:
                self.__threeDigit(num)
            elif len(str(num)) == 4:
                self.__fourDigit(num)
            else:
                self.__fiveDigit(num)
            

k = Kaprekar()
k.run(1978)