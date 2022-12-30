# 导入
import re

pattern = r'\d\.\d+'  # \d匹配0-9的整数  匹配一个整数一次或多次
s = 'I study Python 3.9 everyday'
match = re.match(pattern, s, re.I)
print(match)

s2 = '3.10 python i study every day'
match2 = re.match(pattern, s2, re.I)
print(match2)
print('匹配值的起始位置：', match2.start())
print('匹配值的结束位置：', match2.end())
print('匹配区间的位置元组：', match2.span())
print('待匹配的字符串：', match2.string)
print("匹配的数据:", match2.group())

'''常用的正则处理方法'''
s = 'I study Python 3.9 everyday Python2.10 I love you'
s2 = '4.10python i study every day'
s3 = 'I study Python everyday'
match = re.search(pattern, s)
match2 = re.search(pattern, s2)
match3 = re.search(pattern, s3)
print(match)
print(match2)
print(match3)
# search只匹配第一个对象


print(re.findall(pattern, s))
print(re.findall(pattern, s2))
print(re.findall(pattern, s3))
# findall找出所有匹配对象

#字符串的替换
pattern='黑客|破解|反爬'
s='我想学习python，想破解一些VIP视频，python可以实现无底线反爬吗'
re.sub(pattern,'xxx',s)
print(re.sub(pattern,'xxx',s))

s2='https://www.baidu.com/?wd=ysj&ie=utf-7&tn=baidu'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)