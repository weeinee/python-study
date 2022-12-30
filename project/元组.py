"""元组"""
'''python内置的数据结构之一，是一个不可变序列'''
'''可变序列：列表 字典 ；可以对序列执行增删改操作，对象地址不发生改变'''
'''不可变序列：字符串 元组；没有增删改的操作'''
lst = [10, 20, 30]
print(id(lst))
lst.append(300)
print(lst)
print(id(lst))

#  不可变
s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
"-------------元组的创建---------------"
# 1.直接用（）
t = ('python', 'world', 98)
print(t)
print(type(t))

t2 = 'python', 'world', 98  # 省略了小括号
print(t2)
print(type(t2))
'''元组中只有一个元素需要逗号和小括号'''
t3 = ('python',)
print(type(t3))

# 2.使用内置函数tuple（）
t1 = tuple(('python', 'hello', 96))  # 两层小括号
print(t1)
print(type(t1))
'''空元组的创建方式'''
'''空列表的创建方式'''
lst = []
lst1 = list()

d = {}
d1 = dict()

# 空元组
t4 = ()
t5 = tuple()

print("空列表", lst, lst1)
print("空字典", d, d1)
print("空元组", t4, t5)

t5=(10,[20,30],9)
print(t5)
print(type(t5))
print(t5[0],type(t5[0]),id(t5[0]))
print(t5[1],id(t5[1]))
print(t5[2])

'''尝试将t5[1]修改成100'''
print(id(100))
'''由于[20,30]是列表，列表是可变序列，所以可以添加元素，而列表的内存地址不变'''
t5[1].append(100)
print(t5,id(t5[1]))


 # 元组的遍历
t6=('python','world',98)
print(t6[0])
print(t6[1])
for item in t6:
    print(item)