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

    def info(self):
        super().info()
        print('学号：', self.stu_nu)  # 重写父类中的方法


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)
stu.info()
