class User:
    def __init__(self, name='unknown', age=18):
        self.__name = name #_nameClass__nameField
        self._age = age
        self._email = 'admin@gmai.com'
        self._phone = '+1 555 555 555'

    def __str__(self):
        return f'User: {self.__name}, Age: {self._age}'

    def show_user(self):
        return f'User: {self.__name}, Age: {self._age}'

user1 = User("Bob",30)
user2 = User(name="Bob")
user3 = User(age=20)
user4 = User()
print(user1._User__name)
#print(user1.show_user())

#SOLID S -Single Responsibility Principle
# __new__ - створення об'єкта
# __init__ - ініціалізація об'єкта




#print(isinstance(user,object))
# print(type(True-True))
# print(type(True+10-3+1.4))
#print(int.__subclasses__())
# print(bool.__bases__)
# print(object.__bases__)
