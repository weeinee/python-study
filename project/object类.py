class Student:  # 默认继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0}，今年{1}岁'.format(self.name, self.age)


stu = Student('张三', 20)
print(dir(stu))
print(stu)  # 不输出内存地址了，默认调用__str__方法
print(type(stu))