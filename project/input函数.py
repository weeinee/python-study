# 输入函数input
present = input('大圣想要什么礼物？')
print(present, type(present))  # str类型

# input的高级使用
# 从键盘录入两个整数，计算两个整数的和
a = input('请输入一个加数：')
b = input('请输入另一个加数：')
print(type(a), type(b))
print(a+b)  # 简单拼接str
print(int(a) + int(b))  # 默认为str，需要转类型，或者用a=int(a)，转后输出a+b即可，或者用a=int(input('请输入一个加数：'))，提前转换