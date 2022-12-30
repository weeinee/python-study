"""字符串的拼接"""
# 使用 + 拼接
s1 = 'hello'
s2 = 'world'
print(s1 + s2)

# 使用join方法拼接
print(''.join(['hello', 'world']))
print('*'.join([s1, s2]))

# 直接拼接
print('hello''world')

# 使用格式化字符串
print('%s%s' % (s1, s2))
print('{0}{1}'.format(s1, s2))

'''字符串的去重'''
s = 'sdfghjnmsdfgthjsdfghjsdfgty'
# 字符串的拼接及not in
new_s = ''
for item in s:
    if item not in new_s:
        new_s += item
print(new_s)

# 使用索引+not in
new_s2 = ''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2 += s[i]
print(new_s2)

# 通过集合进行去重+列表排序
new_s3 = set(s)  # 结果是集合
print(new_s3)
lst = list(new_s3)
lst.sort(key=s.index)  # 排序的关键字
print(''.join(lst))

'''列表元素的去重'''
lst=['金星','木星','水星','火星','土星','金星','木星','水星','火星','土星','金星','木星','水星','火星','土星']
new_lst=[]
#遍历+ not in
for item in lst:
    if item not in new_lst:
        new_lst.append(item)
print(new_lst)

#遍历+ not in
new_lst2=[]
for i in range(len(lst)):
    if lst[i] not in new_lst2:
        new_lst2.append(lst[i])
print(new_lst2)

#使用集合去重
s_lst=set(lst)
new_lst3=list(s_lst)
new_lst3.sort(key=lst.index)
print(new_lst3)

