# print(dir(object))
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('Jack', 20)  # x是C的一个实例对象
print(x.__dict__)  # 以字典的形式展示实例对象的属性和值
print(C.__dict__)  # 以字典的形式，展示类对象的属性和方法字典
print('---------------------------------------------')
print(x.__class__)  # 输出实例对象所属的类型
print(C.__bases__)  # 输出类对象的父类类型的元组  (, )
print(C.__base__)  # 输出最近一个父类（基类）(AB)谁在前边输出谁
print(C.__mro__)  # 类的层次结构 (, , , )
print(A.__subclasses__())  # 子类列表，输出类对象的子类
