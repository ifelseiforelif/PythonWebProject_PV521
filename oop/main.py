from unittest import case

from Student import *
from abc import ABC, abstractmethod
# a - abstract b - base c-class

class ITransport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(ITransport):
    def move(self):
        print("Car moved")

class Bus(ITransport):
    def move(self):
        print("Bus moved")


def drive(tr):
    if isinstance(tr,ITransport):
        tr.move()

Tank = type("Tank",(ITransport,),{
        'move':lambda self:print("Tank moved")
    })

def main():
    id = int(input("Enter 1 - Car, 2 - Bus, 3 - Tank: "))
    tr = None
    match id:
        case 1:
            tr = Car()
            pass
        case 2:
            tr = Bus()
            pass
        case 3:
            tr = Tank()
            pass
        case _:
            print("Invalid input")
    if tr is not None:
        drive(tr)
    # drive(Car())
    # drive(Bus())
    # drive(type("Tank",(Transport,),{
    #     'move':lambda self:print("Tank moved")
    # })())
    # s = StudentOnline.from_string("Ivan:20")
    # print(type(s))
    # set1 = {1,2,4}  # create set
    # set2 = {2,4,3,5,11,13}
    # un = set1.difference(set2)
    # print(un) # 2,3,4
    # ^ XOR true ^ false =>true
    # set1.add(2)
    # print(set1)
    # d2 = dict(name="Tom", surname="Due")
    # d2["name"] = "Bob"
    # for item in d2.items():
    #     print(item)
    # cities_1 = {"Київ", "Львів", "Одеса", "Харків"}
    # cities_2 = {"Львів", "Одеса", "Дніпро", "Полтава"}
    # cities_3 = cities_1 - cities_2
    #
    # print("\nПерша множина міст:", cities_1,sorted(cities_1))
    #
    # cities1 = {"Київ", "Львів", "Одеса"}
    # cities2 = {"Львів", "Харків", "Одеса"}
    # common_cities = cities1 & cities2
    # print("\nСпільні міста:", common_cities)

    # Higher Order Function
    # get_sum = lambda x,y:x+y
    # print(get_sum(4,5))
    # li = [7,4,8,9,11,10,-3,-5,10]
    # result = list(map(lambda x:x**2,li))
    # print(f" func map: {result}")
    #
    # result = list(filter(lambda x:x%2==0,li))
    # print(f" func filter: {result}")
    #
    # positive_or_neg = lambda num: "positive or zero" if num>=0 else "negative"
    # print(positive_or_neg(-10))
    # print(positive_or_neg(10))
    # print(positive_or_neg(0))
    #
    # test_func = lambda *arg: arg[0]*3
    # print(test_func(5,6,8,3,8,0))
    #
    # test_func = lambda **arg: arg.values()
    # print(test_func(name="Bob", age=18))
    #show_message()

if __name__ == '__main__':
    main()


def is_negative(num):
    return num<0

def my_decorator(func):
    def wrapper():
        print("Start text")
        func()
        print("End text")
    return wrapper

@my_decorator
def show_message():
    print("Hi Python")