#输入学生姓名，增加到一个列表st中，直到输入的姓名为空为止，最后输出st。

st=[]

while True:
	s = input()
	if s != "":
		st.append(s)
	else:
		break

print(st)