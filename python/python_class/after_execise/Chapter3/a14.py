#一球从80米高度自由下落，每次落地后返回原高度的一半，再落下。求它在第10次落地时共经过多少米？第10次反弹多高？



height = 80
amountLength = 0
times = 10

for i in range(0,times):
	amountLength = amountLength + height
	height = height / 2
	amountLength = amountLength + height

print("10次总共走过%f米,第十次反弹高度为%f米" % (amountLength,height))
