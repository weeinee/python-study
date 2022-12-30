"""列表"""
a = 10  # 变量存储的是一个对象的引用
# 列表存储的是多个对象的引用，每个对象有自己单独的id，type，value
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

'''创建列表'''
# 创建列表的第一种方式：[]
lst1 = ['hello', 'world', 98]
print(lst1)
print(lst1[0], lst1[-1])  # -1为最后一个元素
# 创建列表的第一种方式：[]
lst1 = ['hello', 'world', 98, 'hello']
print(lst1)
print(lst1[0], lst1[-4])  # -4为重复元素
# 创建列表的第二种方式：使用内置函数list()
lst2 = list(['hello', 'world', 98])


'''特点'''
'''
1.列表元素按照顺序有序排序
2.索引映射唯一一个数据
3.列表可以存储重复数据
4.任意数据类型混存
5.根据需要动态分配和回收内存
'''


# 获取指定元素的索引
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))  # 如果列表中有相同元素，只返回列表中相同元素的第一个元素的索引
# print(list.index('Python'))  # 找不到
# 在指定的start和stop之间进行查找
# print(lst.index('hello', 1, 3))  # 找不到
print(lst.index('hello', 1, 4))
print(lst.index('hello', 0, 4))  # 找第一个


# 获取列表中单个元素
lst = ['hello', 'world', 98, 'hello', 'world', 234]
# 获取索引为2的元素（正向索引从0到N-1）
print(lst[2])
# 获取索引为-3的元素（逆向索引从-N到-1）
print(lst[-3])
# 获取索引为10的元素（指定索引不存在，抛出异常）
# print(lst[10])  # IndexError: list index out of range


# 获取列表中多个元素
# 切片操作
lst = [10, 20, 30, 40, 50, 60, 70, 80]
# start=1,stop=6,step=1
# print(lst[1:6:1])
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段：', id(lst2))
print(lst[1:6])  # 默认步长为1
print(lst[1:6:])  # 默认步长为1
# start=1,stop=6,step=2
print(lst[1:6:2])
# stop=6,step=2,start采用默认,0
print(lst[:6:2])
# start=1,step=2,stop采用默认，最后一个元素N-1
print(lst[1::2])

# step为负数
print(lst[::-1])
# start=7,stop省略,step=-1
print(lst[7::-1])
# start=6,stop=0,step=-2
print(lst[6:0:-2])
# stop，start不能是负数

#列表元素判断及遍历
print('p' in 'python')
print('k' not in 'python')

lst = [10, 20, 'python', 'hello']
# 判断
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)
# 遍历
for item in lst:
    print(item)



# 列表元素添加
# 向列表末尾添加一个元素，标识相同，同一个列表对象
lst = [10, 20, 30]
lst.append(100)
print(lst)

# 列表末尾至少添加一个元素
lst2 = ['hello', 'world']
# lst.append(lst2)   # lst2作为一个元素放入lst末尾
lst.extend(lst2)  # 添加lst2每个元素分别添加到lst末尾
print(lst)

# 列表的任意位置添加一个元素
lst.insert(1, 90)
print(lst)

# 列表的任意位置添加至少一个元素（切片，切掉的位置用新的list代替）
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)


#列表元素删除
lst = [10, 20, 30, 40, 50, 60, 30]
lst.remove(30)  # 从列表中溢出一个元素，如果有重复元素只移除第一个元素
print(lst)
# lst.remove(100)  # ValueError: list.remove(x): x not in list

# pop()根据索引移除元素
lst.pop(1)
print(lst)
# lst.pop(5)  # IndexError: pop index out of range 指定的索引位置不存在，抛出异常
lst.pop()  # 不写参数，默认删除最后一个元素
print(lst)

# 切片操作，删除至少一个元素，将产生一个新的列表对象
new_lst = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_lst)
# 不产生新的列表对象，而是删除原列表中的内容（用空列表进行替代）
lst[1:3] = []
print(lst)
# clear()清空列表  元素
lst.clear()
print(lst)  # []
# del删除列表  对象
del lst
# print(lst)  # NameError: name 'lst' is not defined

# 列表生成式

# 使用列表生成式要求列表中的元素都有一定的规则
lst = [i for i in range(1, 10)]
print(lst)
lst1 = [i*i for i in range(1, 10)]
print(lst1)

# 要求：列表中的元素的值为2,4,6,8,10
lst2 = [i*2 for i in range(1, 6)]
print(lst2)

# 列表元素修改
lst = [10, 20, 30, 40]
# 一次修改一个值
lst[2] = 100
print(lst)
# 切片操作
lst[1:3] = [300, 400, 500, 600]
print(lst)


#列表元素排序
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
# 开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表', lst, id(lst))  # 标识未更改，在原列表上进行的排序

# 通过指定关键字参数，将列表中的元素进行降序排序
# reverse=True 表示降序排序
lst.sort(reverse=True)
print(lst)
# reverse=False 表示降序排序
lst.sort(reverse=False)
print(lst)

# 使用内置函数sorted()对列表进行排序，将产生一个新的列表对象，原列表不发生改变
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst)
# 开始排序
new_lst = sorted(lst)  # 产生新的列表对象
print(new_lst)
# 指定关键字参数，实现列表元素降序排序
desc_lst = sorted(lst, reverse=True)
print(desc_lst)

