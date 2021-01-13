def f():
	st["name"] = "x"


st = {"name": "a", "sex": "male"}

f()
print(st["name"], st["sex"])