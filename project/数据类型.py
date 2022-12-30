"""数据类型"""
"1 整数类型"
# 整数类型：可以表示正数、负数、0
n1 = 90
n2 = 76
n3 = 0
print(n1, type(n1))
print(n2, type(n2))
print(n3, type(n3))

# 整数可以表示为二进制0b，十进制，八进制0o，十六进制0x
print('十进制', 118)  # 默认为十进制
print('二进制', 0b10101111)  # 0b二进制
print('八进制', 0o176)  # 0o八进制
print('十六进制', 0x1EAF)  # 0x十六进制

"2 浮点数类型"
a = 3.14159
print(a, type(a))
n1 = 1.1
n2 = 2.2
print(n1 + n2)  # 可能出现小数位数不确定的情况

# 解决方法：导入模块decimal
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))
n1 = 1.1
n3 = 2.1  # 可能出现小数位数不确定的情况，但是有时浮点数相加也是正常的
print(n1 + n3)  # 结果正常，二进制底层的问题

"3 布尔类型"
f1 = True
f2 = False
print(f1, type(f1))
print(f2, type(f2))

# 布尔值可以转成整数计算
print(f1 + 1)  # 2  True表示1
print(f2 + 1)  # 1  False表示0

"4 字符串类型"
str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = """人生苦短，
我用python"""
str4 = '''人生苦短，
我用python'''
print(str1, type(str1)) # string 单引号和双引号定义的必须在一行
print(str2, type(str2))
print(str3, type(str3)) # string 三引号(三个单或者三个双均可)定义的可以在连续的多行
print(str4, type(str4))

'''数据类型的转换'''
#1.其他类型转字符串
name = '张三'
age = 20
print(type(name), type(age))  # 说明name与age的数据类型不同
# print('我叫' + name + '，今年' + age + '岁')  # +为连接符，将不同类型的数据连接的时候会报错，解决方法：类型转换
print('我叫' + name + '，今年' + str(age) + '岁')  # 将int类型通过str()函数转成了str类型
print('------------str()将其他类型转成str类型------------')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))

#2.其他类型转整数型
print('------------int()将其他类型转成int类型------------')
s1 = '128'
f1 = 98.7
s2 = "76.77"
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))  # 将str转成int，前提是字符串为数字串
print(int(f1), type(int(f1)))  # float转成int，截取整数部分，舍弃小数部分
# print(int(s2), type(int(s2)))  # 将str转成int类型，报错，因为字符串为小数串
print(int(ff), type(int(ff)))  # 将bool类型转成对应的数字
# print((int(s3), type(int(s3))))  # str转为int，字符串必须为数字串，且必须为整数串

#3. 其他类型转浮点型

print('------------float()将其他类型转成float类型------------')
s4 = '128.98'
s5 = "76"
fff = True
s6 = 'hello'
i = 98
print(type(s4), type(s5), type(fff), type(s6), type(i))
print(float(s4), type(float(s4)))
print(float(s5), type(float(s5)))  # int转为float，后面加.0
print(float(fff), type(float(fff)))  # 后面加.0
# print(float(s6), type(float(s6)))  # 报错，str里面是字符串不能转为float
print(float(i), type(float(i)))  # int转为float，后面加.0

#注释的使用
# coding:gbk
# 为ANSI编码，不加的话为UTF-8编码：coding:UTF-8，要写在最前面

# 输出功能（单行注释）
print('hello')

'''嘿嘿，
我是
多行注释'''
