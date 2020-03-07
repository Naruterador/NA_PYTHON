import sys

class Calendr(object):
    
    def __init__(self):
        self.mouth_day = [31,28,31,30,31,30,31,31,30,31,30,31]
        self.weekday = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        self.year = 0
        self.mouth = 0
        self.day = 0
        self.rightday = 0

        
    
    def __leap(self,year):
        '''
        leap_2 = 29
        common_2 = 28
        '''
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
        return False  
        
    
    def __catchday(self,date):
        datelist = date.split('-')
        year = int(datelist[0])
        mouth = int(datelist[1])
        day = int(datelist[2])
        if not self.__checkyear(year):
            print('Wrong year format!')
            return False
        
        if not self.__checkmouth(mouth):
            print('Wrong mouth format!')
            return False

        if not self.__checkday(day):
            print('Wrong day format!')
            return False
        
        if self.mouth == 1:
            self.rightday = day

        '''
        temp = 0 
        if self.mouth > 1:
            for i in self.mouth_day[0:mouth - 1]:
                temp = temp + i
            if self.__leap(year):
                self.rightday = temp + day + 1
            else:
                self.rightday = temp + day
        '''
        
        weekday = self.__whichweekday(self.year,self.mouth,self.day)
        print("当前日期是:%d年%d月%d日   星期:%s" %(self.year,self.mouth,self.day,self.weekday[weekday]))
        return True



    def __whichweekday(self,year,mouth,day):
        #基姆拉尔森（Kim larsson calculation formula）计算公式
        '''
        m >= 3 and m <= 14
        计算公式： W= (d+2*m+3*(m+1)/5+y+y/4-y/100+y/400) mod 7
        在公式中d表示日期中的日数，m表示月份数，y表示年数。
        注意：把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10则换算成：2003-13-10来代入公式计算。
        '''
        if 1 == mouth:
            mouth = 13
            year = year - 1
            weekday = (day + 2 * mouth + 3 * (mouth + 1) // 5 + year + year // 4 - year //100 + year // 400) % 7
        elif 2 == mouth:
            mouth = 14
            year = year - 1
            weekday = (day + 2 * mouth + 3 * (mouth + 1) // 5 + year + year // 4 - year //100 + year // 400) % 7
        else:
            weekday = (day + 2 * mouth + 3 * (mouth + 1) // 5 + year + year // 4 - year //100 + year // 400) % 7
        
        
        return weekday



    def __callist(self):
        s1 = input('input year:')

        if self.__checkyear(int(s1)):
            self.year = int(s1)
        else:
            print('Wrong year format')
            return False

        self.mouth = 0
        for i in range(1,13):
            print('------------------ %d 年 %d 月 ------------------' % (self.year,i))
            print('Mon'+'\t'+'Tue'+'\t'+'Wed'+'\t'+'Thu'+'\t'+'Fri'+'\t'+'Sat'+'\t'+'Sun')
            self.mouth += 1
            self.day = self.__checkmouthday(self.year,self.mouth)
            temp = self.__whichweekday(self.year,self.mouth,1)
            if self.day:
                for i in range(temp):
                    print(' ',end='\t')

                for j in range(1,self.day + 1):
                    if (j + temp - 1) % 7 == 0:
                        print('\n')
                    print(str(j),end='\t')
            print('\n')
            

                

    def __checkmouthday(self,year,mouth):
        if not self.__checkyear(year):
            return False
        
        if not self.__checkmouth(mouth):
            return False

        if 2 == mouth:
            if self.__leap(year):
                self.mouth_day[1] = 29

        days = self.mouth_day[mouth - 1]
        return days
        


                


    
    def __checkyear(self,year):
        if year != "" and year > 0:
            self.year = year
            return True
        return False

    def __checkmouth(self,mouth):
        if mouth != "" and (mouth >= 1 and mouth <= 12):
            self.mouth = mouth
            return True
        return False

    def __checkday(self,day):
        if day != "" and (day >=1 and day <=31):
            if self.mouth == 2:
                if self.__leap(self.year):
                    if day >= 1 and day <= 29:
                        self.day = day
                        return True
                else:
                    if day >=1 and day <= 28:
                        self.day = day
                        return True
            else:
                if day >= 1 and day <= self.mouth_day[self.mouth - 1]:
                    self.day = day
                    return True
        return False           



    def run(self):
        while True:
            print('1.计算某天星期几')
            print('2.打印某年的日历')
            print('3.退出')
            s1 = input('请选择(1,2,3):')
            if '1' == s1:
                p1 = input('yyyy-mm-dd:')
                if not self.__catchday(p1):
                    continue
            elif '2' == s1:
                if not self.__callist():
                    continue
            elif '3' == s1:
                sys.exit(0)
            else:
                print('Wrong input!')  
        


d = Calendr()
d.run()