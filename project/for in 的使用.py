# for-in遍历，对象必须是可迭代对象（字符串、序列等）
for item in 'Python':  # 第一次取出来的是P，将P赋值item，将item的值输出
    print(item)


# range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)


# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为“_”
for _ in range(5):
    print('人生苦短，我用Python')


# 使用for循环计算1到100的偶数
sum1 = 0
for item in range(1, 101):
    if item % 2 == 0:
        sum1 += item
print('1到100的偶数和为：', sum1)


# 使用for循环计算100到999之间的水仙花数（三位数，各个位数的三次方之和等于本身，153）
for item in range(100,1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge ** 3 + bai ** 3 + shi ** 3 == item:
        print(item)