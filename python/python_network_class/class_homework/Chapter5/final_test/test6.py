def save(s):
    f = open("test.txt", "wt")
    f.write(s["name"] + "\n")
    f.write(s["sex"] + "\n")
    f.write(s["age"] + "\n")
    f.close()


def read():
    f = open("test.txt", "rt")
    name = f.readline()
    sex = f.readline()
    age = f.readline()
    print(name, sex, age, sep="")
    f.close()


s = {"name": "xxx", "sex": "male", "age": "20"}
save(s)
read()
