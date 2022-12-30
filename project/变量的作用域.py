def fun(a, b):
    c = a + b
    print(c)  # c称为局部变量，因为c是再函数体内部定义的变量，a，b为函数的形参，组哟用范围也在函数内部，相当于局部变量


# print（c，a） 因为ac超出了起作用的范围

name = 'wdk'
print(name)


def fun2():
    print(name)


# 调用函数
fun2()


def fun3():
    global age  # 函数内部定义的变量，局部变量，局部变量使用global生命，这个变量实际上就变成了全局变量
    age = 20
    print(age)


fun3()
print(age)
