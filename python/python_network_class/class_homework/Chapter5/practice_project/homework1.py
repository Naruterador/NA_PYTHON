'''
项目目标
这个项目是通过面向对象的方法设计教材类Book，包含一个教材ISBN、名称(Title)、作者(Author)、出版社(Publisher)，然后设计教材记录管理类BookList来管理一组教材记录。
程序运行后显示
">"
的提示符号，在
">"
后面可以输入show、insert、update、delete等命令实现记录的显示、插入、修改、删除等功能，执行一个命令后继续显示
">"
提示符号，如果输入exit就退出系统，输入的命令不正确时会提示正确的输入命令，操作过程类似第4章中的学生记录管理项目。

在程序启动时会读取books.txt的教程记录，在程序结束时会把记录存储在books.txt文件中。
'''


class Book:
    def __init__(self, ISBN, Title, Author, Publisher):
        self.ISBN = ISBN
        self.Title = Title
        self.Author = Author
        self.Publisher = Publisher

    def show(self):
        print("%-16s %-16s %-16s %-16s" %
              (self.ISBN, self.Title, self.Author, self.Publisher))


class BookList:
    def __init__(self):
        self.books = []
        
    def show(self):
        print("%-16s %-16s %-16s %-16s" %
              ("ISBN", "Title", "Author", "Publisher"))
        for s in self.books:
            s.show()

    def __insert(self, s):
        i = 0
        while (i < len(self.books) and s.ISBN > self.books[i].ISBN):
            i = i + 1
        if (i < len(self.books) and s.ISBN == self.books[i].ISBN):
            print(s.ISBN + " 已经存在")
            return False

        self.books.insert(i, s)
        print("增加成功")

        return True

    def __update(self, s):
        flag = False
        for i in range(len(self.books)):
            if (s.ISBN == self.books[i].ISBN):
                self.books[i].Title = s.Title
                self.books[i].Author = s.Author
                self.books[i].Publisher = s.Publisher
                print("修改成功")
                flag = True
                break

        if (not flag):
            print("没有这个教材")

        return flag

    def __delete(self, ISBN):
        flag = False
        for i in range(len(self.books)):
            if (self.books[i].ISBN == ISBN):
                del self.books[i]
                print("删除成功")
                flag = True
                break

        if (not flag):
            print("没有这个教材")

        return flag

    def delete(self):
        ISBN = input("ISBN=")
        if (ISBN != ""):
            self.__delete(ISBN)

    def insert(self):
        ISBN = input("ISBN=")
        Title = input("Title=")
        Author = input("Author=")
        Publisher = input("Publisher=")
        if ISBN != "" and Title != "":
            self.__insert(Book(ISBN, Title, Author, Publisher))
        else:
            print("ISBN、教材名称不能空")

    def update(self):
        ISBN = input("ISBN=")
        Title = input("Title=")
        Author = input("Author=")
        Publisher = input("Publisher=")
        if ISBN != "" and Title != "":
            self.__update(Book(ISBN, Title, Author, Publisher))
        else:
            print("ISBN、教材名称不能空")

    def save(self):
        try:
            f = open("books.txt", "wt")
            for b in self.books:
                f.write(b.ISBN + "\n")
                f.write(b.Title + "\n")
                f.write(b.Author + "\n")
                f.write(b.Publisher + "\n")
            f.close()
        except Exception as err:
            print(err)

    def read(self):
        self.books = []
        try:
            f = open("books.txt", "rt")
            while True:
                ISBN = f.readline().strip("\n")
                Title = f.readline().strip("\n")
                Author = f.readline().strip("\n")
                Publisher = f.readline().strip("\n")
                if ISBN != "" and Title != "" and Author != "" and Publisher != "":
                    b = Book(ISBN, Title, Author, Publisher)
                    self.books.append(b)
                else:
                    break
            f.close()
        except:
            pass

    def process(self):
        self.read()
        while True:
            s = input(">")
            if (s == "show"):
                self.show()
            elif (s == "insert"):
                self.insert()
            elif (s == "update"):
                self.update()
            elif (s == "delete"):
                self.delete()
            elif (s == "exit"):
                break
            else:
                print("show:   show Books")
                print("insert: insert a new Book")
                print("update: insert a new Book")
                print("delete: delete a Book")
                print("exit:   exit")
        self.save()


books = BookList()
books.process()

