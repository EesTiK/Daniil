class Student():
    def __init__(self ,name):
        self.__name = name
        self.__secname = ' '
    def get_name(self):
        print(self.__name)
    def set_name(self, name):
        self.__name = name
    def get_secname(self):
        print(self.__secname)
    def set_secname(self, name):
        self.__secname = name
a = Student('lil')
a.set_secname('lol')
a.get_name()
a.get_secname()
a.set_name('lil')
a.set_secname('lol')
a.get_name()
a.get_secname()
b = Student('Danja')
b.get_name()

    