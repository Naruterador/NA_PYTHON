'''
计算s = a + aa + aaa + a...aa的和，其中a为[1,9]之内的一个整数，最后一项有n个a,a与n由键盘输入。
'''



#输入a
a=0
while a <= 0 or a >= 10:
     a = input("Enter a[1,9]:")
     a = int(a)

n = 0
while n <= 0:
     n = input("Enter n:")
     n = int(n)

m = 0
s = 0
for i in range(n):
     m = 10 * m + a
     s = s + m
     if i < n - 1:
          print(m,end="+")
     else:
          print(m,end="=")
print(s)
