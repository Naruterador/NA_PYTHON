#一个数如正好等于它的所有因子之和，则称为完数，例如6的因子有1、2、3，而6=1+2+3，因此6是一个完数。编程序找出1000之内的所有完数。



def perfect_num_check(n):
	k = 0
	for i in range(1,n):
		if n % i == 0:
			k = k + i
		else:
			continue

	if k == n:
		return True
	else:
		return False


for i in range(1,1000 + 1):
	if perfect_num_check(i):
		print(i)