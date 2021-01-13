import time

'''
1.闰年的判断:
判断一年y是否是闰年，只要下面的两个条件之一成立：
y可以被4整除，同时不能被100整除；
y可以被400整除；
'''
def isLeap(y):
    if(y % 400 == 0 or y % 4 == 0 and y % 100 != 0):
        return True
    else:
        return False


'''
2.某月最大天:
不同的月份最大天数不同，1、3、5、7、8、10、12月为31天
2月要么是28天（平年）要么是29天（闰年）
设计maxDays函数返回y年m月最大天数：
'''
def maxDays(y,m):
    d = 30
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d = 31
    elif m == 2:
        d = 29 if isLeap(y) else 28
    return d
'''
3.某月1日是星期几
countDays计算y年m月d日是该年第几天：
'''
def countDays(y,m,d):
    days = d
    if m >= 2:
        days += 31
    if m >= 3:
        days += 29 if isLeap(y) else 28
    if m >= 4:
        days += 31
    if m >= 5:
        days+=30
    if m >= 6:
        days += 31
    if m >= 7:
        days += 30
    if m >= 8:
        days += 31
    if m >= 9:
        days += 31
    if m >= 10:
        days += 30
    if m >= 11:
        days += 31
    if m >= 12:
        days += 30
    return days

'''
4.再根据下面的历法公式计算这一天是星期几：

((y - 1) + (y - 1) // 400 + (y - 1) // 4 - (y - 1) // 100 + countDays(y,m,1)) % 7
'''

'''
5.计算值为0、1、2、3、4、5、6分别对应星期日、一、二、三、四、五、六
编写下面的 countWeek函数计算y年的元旦是星期几：
'''
def countWeek(y,m):
    w = (y - 1) + (y - 1) // 400 + (y - 1) // 4 - (y - 1) // 100 + countDays(y,m,1)
    return w % 7
    

md = maxDays(2020,10)
w = countWeek(2020,10)

'''
6.打印一个月的日历
设每个日期占输出宽度是6个字符，一个单元6个位置，则7个日期占42的字符宽度， 计算y年m月1日是星期w，然后通过：
'''

for i in range(w):
    print("%-6s" % " ",end="")

#7.显示w个空单元，然后使用：
for d in range(1,md + 1):
    print("%-6d" % d,end="")
    w=w + 1
    if w % 7 == 0:
        print()

#8.打印这个月的日历，当w是7的倍数时就换行，打印下一个星期。
