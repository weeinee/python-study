"""字符串的驻留机制"""
'''命令窗口交互'''
'''pycharm对字符串进行了优化处理'''
a = 'python'
b = "python"
c = '''python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

'''字符串的常用操作'''
# 查询操作
s = 'hello,hello'
print(s.index('lo'))  # 3 查找子串substr第一次出现的位置，如果查找的子串不存在则抛出valueError
print(s.find('lo'))  # 3  查找子串substr第一次出现的位置，如果查找的子串不存在则返回-1
print(s.rindex('lo'))  # 9 查找子串substr最后一次出现的位置，如果查找的子串不存在则抛出valueError
print(s.rfind('lo'))  # 9 查找子串substr最后一次出现的位置，如果查找的子串不存在则返回-1

print(s.find('k'))
print(s.rfind('k'))

# 大小写转换
s = 'hello python'
a = s.upper()
print(a, id(a))  # 转成大写之后产生新的字符串对象
print(s, id(s))
print(s.lower(), id(s.lower()))  # 转成小写之后产生新的字符串对象
print(s, id(s))
print(s.lower() == s)
print(s.lower() is s)

s2 = 'hello,Python'
print(s2.swapcase())  # 大小写转换 大写变小写 小写变大写
print(s2.capitalize())  # 第一个字母大写 其余的变成小写
print(s2.title())  # 首字母大写

'''字符串内容的对齐操作'''
# center（） 居中对齐
s = 'hello,Python'
print(s.center(20, '*'))  # 宽度20，填充符*
# ****hello,Python****

# ljust（）左对齐
print(s.ljust(20, '*'))
print(s.ljust(10))

# rjust（）右对齐
print(s.rjust(20, '*'))
print(s.rjust(20))
print(s.rjust(10))  # 小于默认长度 返回原字符

# zfill（）  右对齐 左侧用0填充
print(s.zfill(20))

'''字符串的劈分操作'''
s = 'hello world Python'
lst = s.split()  # 左劈分
print(lst)
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))  # 最大分割次数

print(s.rsplit())  # 右侧劈分
print(s1.rsplit('|'))
print(s1.rsplit(sep='|', maxsplit=1))

#统计子串在字符串中出现的次数
print(s.count('a'))

# 字符串的判断
s = 'hello.python'
print('1.', s.isidentifier())  # 1. False
print('2.', 'hello'.isidentifier())  # 2. True
print('3.', '张三_'.isidentifier())  # 3. True
print('4.', '张三_123'.isidentifier())  # 4. True
# 判断字符是否全由空白字符组成
print('5.''\t'.isspace())
# 判断字符是否全由字母组成
print('6.', 'abc'.isalpha())
# 判断字符是否全由十进制数组成
print('7.', '789'.isdecimal())
# 判断字符是否全由数字组成
print('8.', '789546'.isnumeric())
# 判断字符是否全由字母和数字组成
print('9.', 'hjk456'.isalnum())

'''替换与合并'''
# 替换 replace
s = 'hello,Python'
print(s.replace('Python', 'java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'java', 2))
lst = ['hello', 'java', 'python']
print("|".join(lst))
print(''.join(lst))

t = ('hello', 'java', 'python')
print(''.join(t))

print('*'.join('python'))

'''字符串的比较操作'''
print('apple' > 'app')  # True
print('apple' > 'banana')  # False,相当于97>98
'''比较原始值'''
print(ord('a'), ord('b'))  # 97 98

print(chr(97), chr(98))  # a b

'''== 与 is 的区别
   ==比较的是 value
   is 比较的是id是否相等'''
a = b = 'python'
c = 'python'
print(a == b)
print(b == c)
print(id(a))  # 2447281055472
print(id(b))  # 2447281055472
print(id(c))  # 2447281055472
# 字符串驻留机制


'''字符串的切片操作'''
# 字符串不可变
# 不可增删改 切片将产生新的对象
s = 'hello,Python'
s1 = s[:5]  # 由于没有指定起始位置 从0开始
s2 = s[6:]  # 由于没有指定结束位置 到最后结束
s3 = '!'
newstr = s1 + s3 + s2
print(s1)
print(s2)
print(s3)
print(newstr)
print('-----------------------------')
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('-----------切片[start:end:step]------------------')
print(s[1:5:1])  # 从1截到5（不包含5），步长为1
print(s[::2])  # 默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2
print(s[::-1])  # 默认从字符串的最后一个元素开始，到第一个结束
# 想截取python
print(s[-6::1])  # 索引为-6开始步长为1

