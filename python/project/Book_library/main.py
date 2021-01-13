import codecs
import sys


class BookList(object):

    def __init__(self):
        self.__booklist = []
        temp_dict = {}
        with codecs.open("books.txt", "r+", encoding="utf - 8") as file:
            for i in file.readlines():
                t = i.split(' ')
                temp_dict['ISBN'] = int(t[0].strip('\n'))
                temp_dict['Title'] = t[1].strip('\n')
                temp_dict['Author'] = t[2].strip('\n')
                temp_dict['Publisher'] = t[3].strip('\n')
                self.__booklist.append(temp_dict)
                temp_dict = {}

    #显示当前所有书籍
    def __show(self):
        with codecs.open("books.txt", "r+", encoding="utf - 8") as file:
            for i in file.readlines():
                print(i)
    #插入一本书
    def __insert(self):
        temp_dict = {}

        isbnNum = input("ISBN:")
        if 13 != len(isbnNum):
            print("Wrong ISBN code!")
            return False
        num = self.__searchIsbn(isbnNum)
        if num >= 0:
            print("duplicate code!")
            return False
        temp_dict["ISBN"] = isbnNum

        titleName = input("Title:")
        if titleName != "":
            temp_dict['Title'] = titleName
        else:
            return False

        authorName = input("Author:")
        if authorName != "":
            temp_dict["Author"] = authorName
        else:
            return False

        publisherName = input("Publisher:")
        if publisherName != "":
            temp_dict["Publisher"] = publisherName
        else:
            return False

        self.__booklist.append(temp_dict)

        with codecs.open("books.txt", 'a+', encoding='utf - 8') as f:
            f.write("\r")
            for key, value in temp_dict.items():
                f.write(str(value) + ' ')

    #根据ISBN编号或者书名修改书的各项属性
    def __update(self):
        searchSource = input("Which property you wanna to choose as the condition of modifying item? (input:isbn/title):")
        if "isbn" == searchSource:
            isbnnum = input("ISBN:")
            isbnnumlen = len(isbnnum)
            num = self.__searchIsbn(isbnnum)
            if num >= 0:
                ts = input("Modify ISBN:")
                if ts != "":
                    if 13 != len(ts):
                        print("Wrong ISBN code!")
                        return False
                    else:
                        self.__booklist[num]['ISBN'] = ts
                else:
                    pass

                tn = input("Modify title:")
                if tn != "":
                    self.__booklist[num]['Title'] = tn
                else:
                    pass
                
                ta = input("Modify Author:")
                if ta != "":
                    self.__booklist[num]['Author'] = ta
                else:
                    pass
                
                tp = input("Modify Publisher:")
                if tp != "":
                    self.__booklist[num]['Publisher'] = tp
                else:
                    pass

                with codecs.open("books.txt", 'w+', encoding='utf - 8') as f:
                    for i in range(len(self.__booklist)):
                        for key,value in self.__booklist[i].items():
                            f.write(str(value) + '  ')
                        f.write('\r')

        elif "title" == searchSource:
            print('Developing soon!')
            return False
        else:
            print("Error input!")
            return False

    #根据ISBN编号删除书
    def __delete(self):
        isbnDnum = input("Input ISBN num that you wanna delete:")
        num = self.__searchIsbn(isbnDnum)
        if num >= 0:
            del self.__booklist[num]

            with codecs.open("books.txt", 'w+', encoding='utf - 8') as f:
                for i in range(len(self.__booklist)):
                    for key,value in self.__booklist[i].items():
                        f.write(str(value) + '  ')
                    f.write('\r')
        else:
            print("Can not find this book!")
            return False
            
    #根据ISBN编号查找一本书
    def __searchIsbn(self, ISBN):
        for i in range(len(self.__booklist)):
            if int(ISBN) == self.__booklist[i]['ISBN']:
                return i
        return -1

    def controlPanel(self):
        while True:
            i = input(">")
            if "show" == i:
                self.__show()
            elif "insert" == i:
                if not self.__insert():
                    continue
            elif "update" == i:
                if not self.__update():
                    continue
            elif "delete" == i:
                if not self.__delete():
                    continue
            elif "exit" == i:
                sys.exit(0)
            else:
                print("Please input right command!")

b1 = BookList()
b1.controlPanel()
