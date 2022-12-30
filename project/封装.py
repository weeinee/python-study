class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马x5')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)
        # 名称前加两个下划线表示不希望在外部使用


stu = Student('张三', 20)
stu.show()
# 在类的外部使用name和age
print(stu.name)
# print(stu.age)
print(dir(stu))
print(stu._Student__age)#在类的外部可以通过 _Student __age进行访问
