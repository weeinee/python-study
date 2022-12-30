lst = [88, 89, 90, 98, 00, 99]
print('原列表', lst)
# 遍历列表
'''for index in range(len(lst)):
    if str(lst[index])!='0':
        lst[index]='19'+str(lst[index])#拼接年份后赋值
    else:
        lst[index]='200'+str(lst[index])

#修改后的年份列表
print(lst)'''

# 使用enumerate函数遍历列表
for index, value in enumerate(lst):
    if str(value) != '0':
        lst[index] = '19' + str(value)
    else:
        lst[index] = '200' + str(value)
print(lst)
