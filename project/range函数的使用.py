# range()的三种使用方式
# 第一种：只有一个参数，括号中只有一个值，默认从0开始，默认相差1为步长
r = range(10)
print(r)  # range(0,10)
print(list(r))  # 用于查看range对象中的整数序列  -->list是列表的意思

# 第二种：两个参数，表示开始和结尾，默认步长为1
rr = range(1, 10)
print(list(rr))

# 第三种，三个参数，表示开始、结尾和步长
rrr = range(1, 10, 2)
print(list(rrr))

# 使用in与not in判断整数序列中是否存在指定的整数
print(10 in rrr)
print(9 in rrr)
print(10 not in rrr)

# 好处：只存储对应的参数，内存空间相同
print(range(1, 20, 1))  # [1...19]
print(range(1, 101, 1))  # [1...100]
# 只有在用到range对象时，才计算序列中的相关元素