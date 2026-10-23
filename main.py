#MRO (C3 Linearization)
#Mixin
#iterators
#MVC/MVT (Flask)
import json


#MRO - Method Resolution Order (C3 Лінеарізація)

# class A3:
#     def __init__(self):
#         print("Init A3")
#         super().__init__()
# class A2(A3):
#         def __init__(self):
#             print("Init A2")
#             super().__init__()
# class A1(A2):
#     def __init__(self):
#         print("Init A1")
#         super().__init__()
# class A(A1):
#     def __init__(self):
#         print("Init A")
#         super().__init__()
#
# class B3:
#     def __init__(self):
#         print("Init B3")
#         super().__init__()
#
# class B2(B3):
#     def __init__(self):
#         print("Init B2")
#         super().__init__()
#
# class B1(B2):
#     def __init__(self):
#         print("Init B1")
#         super().__init__()
#
# class B(B1):
#     def __init__(self):
#         print("Init B")
#         super().__init__()
#
# class C(A1,B,A2):
#     def __init__(self):
#         print("Init C")
#         super().__init__()
#
# print(C.mro()) # C B B1 B2 B3 A A1 A2 A3 object
# # print(C.__mro__)


#Mixin - це клас
class JsonSerializerMixin():
    import json
    def to_json(self):
        return json.dumps(self.__dict__, default=str, ensure_ascii=False)


class TimeMixin:
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        from datetime import datetime
        self.created_at = datetime.now()

class User(JsonSerializerMixin, TimeMixin):
    def __init__(self, username: str):
        super().__init__()
        self.username = username

u = User("Олександр")
print(u.to_json())

# def test(*args):
#     print(args)
#
# def test2(*args, **kwargs):
#     print(kwargs)
#
# test2(4,6,7,9,name="Alex", age= 30)
# test(5,7,8,9,3)
# test()
# test(1,3)
