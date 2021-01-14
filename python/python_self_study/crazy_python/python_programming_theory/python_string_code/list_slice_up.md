####列表、字符串、元组、字典的切片输出

python列表切片
 

Python中符合序列的有序序列都支持切片（slice），例如列表，字符串，元组。

     格式：【start:end:step】

     start:起始索引，从0开始，-1表示结束

     end：结束索引

     step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值

    注意切片的结果不包含结束索引，即不包含最后的一位，-1代表列表的最后一个位置索引


start.end,step可选，冒号必须的, 基本含义是从start开始（包括string[start]），以step为步长，获取到end的一段元素（注意不包括string[end]）。
如果step=1，那么就是 string[start],string[start+1],......,string[end-2],string[end-1]，如果step>1，那么
第一为string[start]
第二为string[start+step]
第三为string[start+2*step]，......, 以此类推，最后一个为string[m]，其中m<end,但是m+step>=end。
即索引的变化是从start开始，按step跳跃变化，不断增大，但是不等于end，也不超过end。
如果end超过了最后一个元素的索引，那么最多取到最后一个元素。
start不指定默认0，end不指定默认序列尾，step不指定默认1.
step为正数则索引是增加的，索引沿正方向变化；如何step<0，那么索引是减少的，按负方向变化。
我们不能使用step=0，不然索引就原地踏步不变了。
如果start,end为负数，表示倒数的索引，例如start=-1，则表示len(string)-1, start=-2，表示len(string)-2。

实例1：
s= "abcdefghijk"
print("s---",s)
print("s[0:2]---",s[0:2])
print("s[:2]---",s[:2])
print("s[2:]---",s[2:])
print("s[2,6]---",s[2:6])
print("s[:]---",s[:])
print("s[::,2]---",s[::2])
print("s[0:7:2]---",s[0:7:2])
print("s[8:14])---",s[8:14])
print("s[1:5:2]---",s[1:5:2])
print("s[1:4:2]---",s[1:4:2])
输出结果:
s--- abcdefghijk
s[0:2]--- ab
s[:2]--- ab
s[2:]--- cdefghijk
s[2,6]--- cdef
s[:]--- abcdefghijk
s[::,2]--- acegik
s[0:7:2]--- aceg
s[8:14])--- ijk
s[1:5:2]--- bd
s[1:4:2]--- bd

实例2:
s= "abcdefghijk"
print("s---",s)
print("s[0:-2]---",s[0:-2])
print("s[:-2]---",s[:-2])
print("s[-2:]---",s[-2:])
print("s[-2,6]---",s[-2:6])
print("s[:]---",s[:])
print("s[::,-2]---",s[::-2])
print("s[7,-1:-1]---",s[7:1:-1])
print("s[8:0.-1])---",s[8:0:-1])
print("s[5:1:-2]---",s[5:1:-2])
print("s[4:1.-2]---",s[4:1:-2])
输出结果:
s--- abcdefghijk
s[0:-2]--- abcdefghi
s[:-2]--- abcdefghi
s[-2:]--- jk
s[-2,6]--- 
s[:]--- abcdefghijk
s[::,-2]--- kigeca
s[7,-1:-1]--- 
s[8:0.-1])--- ihgfedcb
s[5:1:-2]--- fd
s[4:1.-2]--- ec

