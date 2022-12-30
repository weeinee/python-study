"""集合"""
'''数据结构之一'''
"与字典的区别，只有key没有value"
'''集合是没有value的字典'''
# 创建集合
# 1.使用{}
s = {2, 3, 4, 5, 5, 6, 7, 7}  # 集合中的元素不允许重复
print(s)

# 2.使用内置函数set（）
s1 = set(range(6))
print(s1, type(s1))

s2 = set([1, 2, 3, 4, 5, 6, 6, 5])
print(s2, type(s2))

s3 = set((1, 2, 3, 5, 5, 6, 89))
print(s3, type(s3))  # 集合中的元素是无序的

s4 = set('python')
print(s4, type(s4))

s5=set({12,4,64,55,66,77,4})
print(s5,type(s5))

#定义一个空集合
s6={}
print(type(s6))#dict

s7=set()
print(type(s7))

s8={''}
print(type(s8))