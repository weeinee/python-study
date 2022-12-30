'''break语句'''
# 从键盘区录入密码，最多录入三次，如果正确就结束循环
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')


# while循环实现
a = 0
while a < 3:
    # 条件执行体
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    # 改变变量
    a += 1




'''continue语句'''
# continue: 结束当前循环，进入下一循环
# 要求：输出1到50之间所有5的倍数（和5的余数为0）
for item in range(1, 51):
    if item % 5 == 0:
        print(item)



# 使用continue
for item in range(1, 51):
    if item % 5 != 0:
        continue
    else:
        print(item)