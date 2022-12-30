"个数可变的位置参数"


def fun(*args):
    print(args)
    # print(args[0])


fun(10)
fun(10, 30)
fun(30, [10, 50, 'a'], 5)

"个数可变的关键字形参"


def fun1(**args):
    print(args)


fun1(a=10)
fun1(a=20, b=30, c=40)
# 结果是一个字典

print()

'''def fun2(*args,*a):
   pass
   以上代码程序会报错，个数可变的位置参数只能有一个
   def fun2(**args,**a):
   pass
   以上代码程序会报错，个数可变的关键字参数只能有一个
   '''


def fun2(*args1, **args2):
    pass


'''def fun2(**args1,*args2):
    pass
    在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求，
    个数可变的位置形参放在个数可变的关键字形参之前
'''


# 函数的参数总结

def fun3(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


# 函数的调用
fun3(10, 20, 30)  # 位置传参
lst = [11, 22, 33]
fun3(*lst)  # 函数调用时，将列表中的每个元素都转换为位置实参传入
fun3(a=100, c=300, b=200)  # 关键字调用
dic = {'a': 111, 'b': 222, 'c': 333}
fun3(**dic)  # 在函数调用时，将字典中的键值都转换为关键字实参传入


def fun4(a, b=10):  # b是在函数的定义处，所以b是形参，而且进行了赋值，所以称b为默认值形参
    print('a=', a)
    print('b=', b)


def fun5(*args):  # 个数可变的位置形参
    print(args)


def fun6(**args2):  # 个数可变的关键字形参
    print(args2)


fun5(10, 20, 30, 40)
fun6(a=11, b=12, c=13)


def fun7(a, b, *, c, d):  # 在*之后的参数只能使用关键字调用
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)


'''函数定义时的形参的顺序问题'''


def fun8(a, b, *, c, d, **args):
    pass


def fun9(*args, **args2):
    pass


def fun7(a, b=10, *args, **args2):
    pass
# 以上形式均不报错



