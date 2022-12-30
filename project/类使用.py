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


# 创建student类的对象
stu1 = Student('张三', 20)  # 实例对象
stu1.eat()  # 调用方法 对象名.方法名（）
print(stu1.name)
print(stu1.age)
stu1.cm()  # 调用方法

print('------------------------------')
Student.eat(stu1)  # 与26行相同
                   #  类名.方法名（类的对象）————>实际上就是方法定义处的self

print('------------------------------')


'''类属性的使用方式'''
print(Student.native_pace)
stu1 = Student('张三', 20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu1.native_pace)

print('--------------------------')
#类方法的使用方法
Student.cm()
#静态方法的使用方法
Student.methord()#直接用类名.方法名

