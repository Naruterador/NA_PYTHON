'''
一个猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
#recursion
def catch_pitch_r(n):
	sum1 = 0
	if 1 == n:
		return 1
	else:
		sum1 = sum1 + (catch_pitch_r(n - 1) + 1) * 2
		return sum1



#loop
def catch_pitch_l(n):
	for i in range(n,0,-1):
		if 10 == i:
			sum1 = 1
		else:
			sum1 = (sum1 + 1) * 2
	return sum1
