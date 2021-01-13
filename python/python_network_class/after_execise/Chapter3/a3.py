#从键盘输入一个字符串，直到回车结束，统计字符串中的大小写英文字母各有多少个。

def count_alp(strs):
	upper = 0
	lower = 0 
	for s in strs:
		if s.isupper():
			upper += 1
		elif s.islower():
			lower += 1
	print("大写字母数量为:%d,小写字母数量为%d" % (upper,lower))

if __name__ == '__main__':
	strs = input("请输入您要计算的字符串:")
	count_alp(strs)