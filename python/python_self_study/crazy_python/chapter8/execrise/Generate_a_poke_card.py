#coding = utf - 8


'''
生成一副牌52张，不含大小王
'''

allcards = {}

flowers = ['spade','heart','clubs','diamond']

for i in flowers:
	for j in range(1,14):
		if j == 1:
			allcards[i+str(j)] = 'A'
		elif j == 11:
			allcards[i+str(j)] = 'J'
		elif j == 12:
			allcards[i+str(j)] = 'Q'
		elif j == 13:
			allcards[i+str(j)] = 'K'
		else:
			allcards[i+str(j)] = j

		

print(allcards)