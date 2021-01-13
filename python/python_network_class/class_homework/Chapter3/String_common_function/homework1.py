#题目：输入三个整数x,y,z，请把这三个数由小到大输出。


m = []
for i in range(0,3):
    n = int(input('input:'))
    m.append(n)
    m.sort()
print (m)
