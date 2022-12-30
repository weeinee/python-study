"""集合元素的判断"""
s = {10, 20, 30, 405, 60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)

'''集合元素的新增'''
s.add(80)  # add 一次添加一个元素
print(s)
s.update({200, 400, 300})  # update 一次至少增加一个元素
print(s)
s.update([100, 99, 8])
s.update((78, 64, 32))
print(s)

'''集合元素的删除'''
s.remove(100)
print(s)
# s.remove(500)
s.discard(500)  # 集合存不存在都删除
print(s)
s.pop()  # pop不能指定参数 只删除任意元素
print(s)
s.pop()
print(s)
s.clear()  # 清空
print(s)

'''集合间的关系'''
# 集合是否相等（元素相同就相等）
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)
print(s1 != s2)  # 集合中的元素是无序的

# 一个集合是否是另一个集合的子集

s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # issubset 子集判断函数
print(s3.issubset(s1))

# 一个集合是否是另一个集合的超集
print(s1.issuperset(s2))
print(s1.issuperset(s3))

# 两个集合是否有交集
print(s2.isdisjoint(s3))  # 有交集：False，没交集:True
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))

# 集合的数学操作
# 1 交集
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)  # 交集操作

# 2 并集
print(s1.union(s2))
print(s1 | s2)

# 3 差集
print(s1.difference(s2))

# 4 对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

'''集合生成式'''
s = {i * i for i in range(10)}
print(s)
