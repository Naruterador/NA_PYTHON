'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

'''
firstParty = ['a','b','c']
secondparty = ['x','y','z']
vslist = []

for i in firstParty:
	for j in secondparty:
		if ('a' == i and 'x' != j):
			vslist.append([i,j])
		elif 'b' == i and ('x' == j or 'y' == j or 'z' == j):
			vslist.append([i,j])
		elif 'c' == i and ('z' != j and 'x' != j):
			vslist.append([i,j])
'''

a = ''
b = ''
c = ''

secondParty = ['x','y','z']

for i in secondParty:
	if 'x' != i and 'z' != i:
		c = i

for i in secondParty:
	if 'x' != i and i != c:
		a = i

for i in secondParty:
	if i != a and i != c:
		b = i


print("a vs %s,b vs %s,c vs %s" % (a,b,c))