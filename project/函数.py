"""函数"""
'''函数的创建和调用'''
"""函数的创建
   def 函数名（[输入参数]）
   函数体
   [return xxx]"""


def calc(a, b):  # a,b 称为形式参数，简称形参，形参的位置是在函数定义处
    c = a + b
    return c


result = calc(10, 20)  # 10，20称为实际参数的值，简称实参，实参的位置是函数调用处
print(result)

"""函数的参数传递"""
# 1 根据位置传递
# 2 根据关键字传递
res = calc(b=10, a=20)  # 等号左侧的变量的名称叫做 关键字参数
print(res)


def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
    return


n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print('n1', n1)
print('n2', n2)

'''在函数调用过程中，进行参数的传递
如果是不可变对象，在函数体内的修改不会影响实参的值 arg1的修改为100，不会影响n1的值
如果是可变对象，在函数体的修改会影响到实参的值 arg2的修改，append（10），会影响到n2的值'''

print(bool(0))
print(bool(8))


def fun1(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


# 函数的调用
print(fun1([15, 67, 85, 96, 74, 23, 54]))

'''
函数的返回值
    （1）如果函数没有返回值【函数执行完毕后，不需要给调用处提供数据】 return可以省略不写
    （2）函数的返回值，如果是一个，直接返回原类型
    （3）函数的返回值如果是多个，返回的结果是元组
    函数在定义时 是否需要返回值视情况而定
'''


# 函数的参数定义
def fun2(a, b=10):
    print(a, b)


# 函数的调用
fun2(100)
fun2(20, 30)

print('hello', end='\t')
print('world')  # 不换行打印
