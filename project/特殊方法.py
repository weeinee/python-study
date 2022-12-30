a = 20
b = 100
c = a + b  # 两个整数类型的相加操作
d = a.__add__(b)

print(c)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('Jack')
stu2 = Student('Mike')

print(stu1 + stu2)  # 实现了两个对象的加法运算，因为在类中编写了__add__()特殊方法

s = stu1.__add__(stu2)
print(s)  # 同上

# __len__()
lst = [11, 22, 33, 44]
print(len(lst))  # len是内置函数len
print(lst.__len__())  # 同上

print(len(stu1))  # __len__()
