# 打印函数
print('hello world')

# print会输出①数字②字符串（必须加引号）③含有运算符的表达式（例如 3+1 其中3，1是操作数，+是运算符）（进行运算)
print(3 + 1)
print(5 * 6)

# print还可以输出内容目的地
fp = open("D:/text.txt", 'a+')
print("helloworld", file=fp)
fp.close()  # 注意：1.指定的盘符存在 2.使用file=fp

# print（）函数的输出形式
print('hello', 'world', 'python')  # 不换行输出
print('hello\n', 'world')  # 换行输出

'''转义字符'''
# 换行   \n [newline]
# 回车   \r [return]
# 水平制表符  \t [tab]
print('hello\tworld')  # \t占四个位
print('helloooo\tworld')
# 退格   \b
print('hello world\b')  # 输出hello worl
# 原字符：不希望字符串中转义字符起作用，就使用原字符，在字符串首加r或R
print(r'hello\nworld')  # 输出hello\nworld

# 二进制
print(chr(0b100111001011000))  # 0b表示为十六进制

print(ord('乘'))  # 十进制为20056

# 标识符和保留字
import keyword

print(keyword.kwlist)
# 输出结果不可以作为变量名称

'''变量的定义和使用'''
name = '玛利亚'
print(name)

print('标识', id(name))  # 变量有标识id(obj)
print('类型', type(name))  # 变量有类型type(obj)
print('值', name)  # 变量有值value

'''变量的多次赋值'''
name = '玛利亚'
print(name)
name = '出溜冰'  # 变量的多次赋值，name指向新的空间，
print(name)  # 原来的地方没有东西了，被称为内存垃圾，垃圾回收机制进行回收
