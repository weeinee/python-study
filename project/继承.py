class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_nu):
        super().__init__(name, age)
        self.stu_nu = stu_nu


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

stu.info()
teacher.info()


# 子类可以有多个父类
class A(object):
    pass


class B(object):
    pass


class C(A, B):
    pass


'''但是，继承的时候，怎么指定继承哪一个父类呢'''
'''假设A有姓名B有年龄 调用写法 A.__init__(self,name) B__init__(self,age)'''
