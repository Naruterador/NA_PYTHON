'''
题目：输入某年某年某月某日，判断这一天是这一年的第几天？
1.普通年能被4整除且不能被100整除的为闰年。(如2004年就是闰年,1900年不是闰年)
2.世纪年能被400整除的是闰年。(如2000年是闰年,1900年不是闰年)
'''


year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 <= month <= 12:
	sum1 = months[month - 1]
else:
	print('data error')

sum1 += day     #sum1 = sum1 + day
leap = 0

if (year % 400) or ((year % 4 == 0) and (year % 100 != 0)):
	leap = 1
if (leap == 1) and (month > 2):
	sum1 += 1 #sum1 = sum1 + 1
	
print('it is the %dth day.' % sum1)

