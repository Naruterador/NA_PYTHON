'''
1、案例描述
设计程序判断一个字符串是否对称。
 
2、案例分析
方法一：编写一个函数reverse(s)把字符串s反向，然后把反向的结果与原来的字符串比较，如果一样就说明是对称的。

方法二：有一种判别对称的方法，用i,j表示左右的下标，逐步比较(s[0],s[len(s)-1]) , (s[1],s[len(s)-2]) ,......, 如果由不相等的，一定不对称，如果全部比较完毕都相等，则对称。
'''
'''
#方法一：
def reverse(s):
  t = ""
  for i in range(len(s)-1,-1,-1):
      t = t + s[i]
  return t

def isSymmetry(s):
  t = reverse(s)
  if s == t:
    return 1
  else:
    return 0

s = input("Enter a string: ")

if isSymmetry(s) == 1:
  print("对称")
else:
  print("不对称")
'''


#方法二：
def isSymmetry(s):
  i = 0
  j = len(s)-1
  
  while i <= j:
    if s[i] != s[j]:
      return 0
    i = i + 1
    j =j - 1
  return 1
 
s = input("Enter a string: ")

if isSymmetry(s) == 1:
    print("对称")
else:
    print("不对称")

