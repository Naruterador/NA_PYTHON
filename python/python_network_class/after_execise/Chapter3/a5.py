#输入若干个同学的成绩，计算平均成绩，输入的成绩为负数或大于100时表示结束输入。


grades = input("请输出每个同学的成绩，以空格隔开:")
gradelist = grades.split()

amount_grade = 0
members = len(gradelist)
del_grade = 0
for i in range(members):
	if int(gradelist[i]) < 0 or int(gradelist[i]) > 100:
		del_grade += 1
	else:
		amount_grade = amount_grade + int(gradelist[i])

aver_grade = amount_grade / (members - del_grade)

print(aver_grade)
