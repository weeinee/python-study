# 用{}去定义一个列表
# 可以添加元素 删除 修改元素
scores = {'张三': 100, '李四': 200, '王五': 45}
print(scores)
print(type(scores))
'''第二种创建方式'''
student = dict(name='jack', age=20)
print(student)
'''空字典'''
d = {}
print(d)
'''获取字典中的元素'''
'''第一种方式 使用[]'''
print(scores['张三'])
'''第二种方法 使用get（）'''
print(scores.get('张三'))
print(scores.get('陈留'))
print(scores.get('麻子', 99))  # 99是在查找
'''字典当中的增 删 改'''
print('张三' in scores)
print('张三' not in scores)

# del scores['张三']  # 删除指定的key-value对
# scores.clear()  #清空字典的元素
print(scores)
scores['陈留'] = 98
print(scores)
scores['陈留'] = 100
print(scores)

'''获取字典视图的几种方法'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的key组成的视图转换成列表

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对
items = scores.items()
print(items)
print(list(items))  # 转换之后的列表元素是由元组组成的

'''字典元素的遍历'''
for i in scores:
    print(i, scores[i], scores.get(i))

'''字典的特点'''
d = {'name': '张三', 'name': '李四'}
print(d)
'''key不允许重复'''
d = {'name': '张三', 'nikemane': '张三'}  # value可以重复
print(d)

lst = [10, 20, 30]
lst.insert(1, 100)  # insert 插入函数
print(lst)
'''字典中的key必须是不可变对象 整数 字符串等 列表不是'''
# 查询速度快但会浪费内存空间

"""字典生成式"""
items = ['fluits', 'books', 'others']
prices = [96, 78, 85]
# lst = zip(items,price)
# print(list(lst))
d = {key.upper(): value for key, value in zip(items, prices)}
print(d)
