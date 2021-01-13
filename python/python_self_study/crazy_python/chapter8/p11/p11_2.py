#coding = utf - 8


'''
程序可以时候for循环来遍历生成器，相当于不断地使用next()函数来获取生成器的下一个值

'''

def test(val,step):
	print("------函数开始执行--------")
	cur = 0
	#遍历0~val
	for i in range(val):
		#cur添加 i*step
		cur = cur + i * step
 
		#print(cur,end=" ")
		yield cur

t = test(10,2)
print("===============")
#获取生成器的第一个值
print(next(t))          #生成器被冻结在yield处
#获取生成器的第二个值
print(next(t))          #生成器再次被冻结在yield处

for i in t:
	print(i,end =  " ")

'''
for循环输出结果为:
6 12 20 30 42 56 72 90

由于前面已经使用next()函数获取了生成器的前两个值，因此循环从第三个数6开始

'''