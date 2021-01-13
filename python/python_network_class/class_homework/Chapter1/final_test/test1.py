
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示,60-80分之间的用B表示，60分以下的用C表示。
'''

score = int(input('input score:'))

if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else:
	grade = 'E'

print ('%d belongs to %s' % (score,grade))

