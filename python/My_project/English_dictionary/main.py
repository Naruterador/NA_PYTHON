class EnglishDic(object):
    
    def __init__(self):
        self.__words = [{"word": "about", "note": "在附近，关于"},\
         {"word": "post", "note": "邮寄、投递"}]


    def insert(self,word,note):
        newword = {}
        num = self.__search(word)
        if num >= 0:
            newword["word"] = word
            newword["note"] = note
            self.__words.append(newword)
        else:
            print("The duplicate word!") 

    def update(self,word,note):
        num = self.__search(word)
        if num >= 0:
            self.__words[num]["note"] = note
        else:
            print("Could not find word that you entered!")

    def search(self,word):
        num = self.__search(word)
        if num >= 0:
            print(self.__words[num])
        else:
            print("Can not find that word!")
    

    def __search(self,word):
        low = 0
        high = len(self.__words) - 1
        mid = (low + high) // 2
        while low <= high:
            if self.__words[mid]['word'] == word:
                return mid
            if self.__words[mid]['word'] < word:
                low = mid + 1
                mid = (low + high) // 2
            if self.__words[mid]['word'] > word:
                high = mid - 1
                mid = (low + high) // 2
        return False

    def show(self):
        print(self.__words)


e = EnglishDic()
e.insert("fuck","干你娘")
e.update("about","大概")
e.search("post")
e.show()