# 类的创建
class Student:  # Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写 其余小写
    native_pace = '黑龙江'  # 直接写在类里的变量称为类属性

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值操作，将局部变量name的值赋给实体属性 
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def methord():  # 不写self
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，我使用了classmethod进行修饰')


# 在类之外定义的为函数，类之内定义的为方法
def dirnk():
    print('喝水')
