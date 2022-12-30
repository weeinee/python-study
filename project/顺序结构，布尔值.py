#程序的顺序结构

# 把大象装在冰箱一共分几步
print('-----程序开始------')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('-----程序结束------')

# 学会打断点，从开始到结束，小虫子，按从上到下按钮

# 对象的布尔值

# 测试对象的布尔值
# 可以把对象直接放在if条件语句中判断，写下一步语句
print('---------以下对象的布尔值为False-----------')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))  # 长度为0的字符串对象
print(bool(""))  # 长度为0的字符串对象
print(bool([]))  # 空列表[]
print(bool(list()))  # 空列表
print(bool(()))  # 空元组
print(bool(tuple()))  # 空元祖
print(bool({}))  # 空字典
print(bool(dict()))  # 空字典
print(bool(set()))  # 空集合

print('---------除以上，其他对象的布尔值为True-----------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))  # 不是空字符串