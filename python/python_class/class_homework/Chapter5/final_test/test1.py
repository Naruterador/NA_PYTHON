def save(s):
    f = open("test.txt", "wt")
    f.write(s["name"])
    f.write(s["sex"])
    f.write(s["age"])
    f.close()

def read():
    f = open("test.txt", "rt")
    s = f.read()
    print(s)
    f.close()


s = {"name": "xxx", "sex": "male", "age": "20"}
save(s)
read()