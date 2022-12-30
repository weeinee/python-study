'''格式化字符串'''
# 方式一 %做占位符
name = '张三'
age = 20
print("我叫%s,今年%d岁" % (name, age))
# 方式二 {}做占位符
print("我叫{0},今年{1}岁".format(name, age))

'''format用法'''
# 模板字符串.format(逗号分隔的参数)
s = 'helloworld'
print('{0:*<20}'.format(s))  # <:左对齐 用*填充 长度20
# 输出结果 helloworld**********
print('{0:*>20}'.format(s))  # 右对齐
print('{0:*^20}'.format(s))  # 居中对齐
print(s.center(20, '*'))  # 实现居中的效果

# 千位分隔符(只适用于整数和浮点数)
print('{0:,}'.format(98765465434))
print('{0:,}'.format(9876543.5453))

# 浮点数小数部分的精度
print('{0:.2f}'.format(3.1415936))
# 或者是字符串类型的最大显示长度
print('{0:.5}'.format('helloworld'))

# 整数类型
a = 425
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(a))

# 浮点数类型
b = 3.1415926
print('{0:.2},{0:.2E},{0:.2e},{0:.2%}'.format(b))

# 方式三 f-string
print(f'我叫{name}，今年{age}岁')

print('%10d' % 99)  # 10表示宽度
print('%.3f' % 3.1415926)  # .3表示小数点后三位
# 同时表示宽度和精度
print('%10.3f' % 3.1415926)  # 一共总宽度为10，小数点后三位
print('hellohello')

print('{0:.3}'.format(3.1415926))  # .3表示的是一共三位数
print('{0:.3f}'.format(3.1415926))  # .3f表示的是三位小数
print('{:10.3f}'.format(3.1415926))  # 同时设置精度和宽度一共10位 三位是小数

'''字符串的编码转换'''

s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK这种编码格中 一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文占3个字节

# 解码
# byte代表就是一个二进制数据
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
# print(byte.decode(encoding='UTF-8')) UnicodeDecodeError:
# 用什么编码就用什么解码
byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))

# 数据的验证和处理
# 所有字符都是数字(十进制数)
print('123'.isdigit())  # True
print('一二三'.isdigit())  # False
print('0b1001'.isdigit())  # False

# 所有字符都是数字（阿拉伯数字 罗马数字等）
print('1234'.isnumeric())  # True
print('一二三'.isnumeric())  # True
print('0b1001'.isnumeric())  # False
print('壹贰叁'.isnumeric())  # True

# 所有都是字母（英文 中文）
print('hello你好'.isalpha())  # True
print('hello你好123'.isalpha())  # False

# 所有都是字母加数字
print('hello你好123'.isalnum())  # True
print('hello你好123...'.isalnum())  # False
print('hello你好一二三'.isalnum())  # True
print('hello你好壹贰叁'.isalnum())  # True

# 所有都是小写字母
print('HELLOworld'.islower())
print('helloworld'.islower())

# 所有都是大写字母
print('HELLOworld'.isupper())
print('HELLOWORLD'.isupper())

# 是否是首字母大写
print('Helloworld'.istitle())
print('Hello World'.istitle())

# 是否都是空白字符
print('\t'.isspace())
print('   '.isspace())
print('\n'.isspace())


