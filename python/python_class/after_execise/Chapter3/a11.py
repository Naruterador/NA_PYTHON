#小华今年12岁，他妈妈比他大20岁，编写程序计算多少年后他妈妈年龄比他大一倍。

sonAge = 12
motherAge  = 32
year = 0

for i in range(1,100):
	if motherAge == 2 * sonAge:
		print(year)
		break
	else:
		year += 1
		motherAge += 1
		sonAge += 1
