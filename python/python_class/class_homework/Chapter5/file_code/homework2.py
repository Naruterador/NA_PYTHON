def save(s):
    f = open("test.txt", "wb")
    s = s.encode()
    f.write(s)
    f.close()


def read():
    f = open("test.txt", "rt")
    s = f.read()
    print(s)
    f.close()


save("我们\nwe")
read()
