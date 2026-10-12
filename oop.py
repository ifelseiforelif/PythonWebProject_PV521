from User import *

user1 = User("Bob",30)

user1+2
print(user1)
user1+User("Alice", 25)
print(user1)


# user2 = User("Bob",30)
# user3 = User("Bob",30)
# print(user1)
# try:
#     user1.age += 1
#     print(user1)
#     user1.age = 40
#     print(user1)
#     print(User.get_counter())
# except Exception as e:
#     print(e)

# user2 = User(name="Bob")
# user3 = User(age=20)
# user4 = User()

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

#class Counter:
#     counter = 10
#     def __init__(self):
#         self.counter+=1
#
# a = Counter()
# print(a.counter)
