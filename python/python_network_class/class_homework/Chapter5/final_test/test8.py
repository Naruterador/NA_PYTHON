def save(s):
    f = open("test.txt", "wt")
    f.write(s["name"] + "\n")
    f.write(s["sex"] + "\n")
    f.write(s["age"] + "\n")
    f.close()


def read():
    f = open("test.txt", "rt")
    name = f.readline().strip("\n")
    sex = f.readline().strip("\n")
    age = f.readline().strip("\n")
    print(name)
    print(sex)
    print(age)
    f.close()


s = {"name": "xxx", "sex": "male", "age": "20"}

save(s)
read()
