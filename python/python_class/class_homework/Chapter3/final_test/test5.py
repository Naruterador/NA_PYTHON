def f(st):
	st.append('x')
	return st


st = ['a']
st = f(st)
print(st)