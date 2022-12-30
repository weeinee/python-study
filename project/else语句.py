# 从键盘区录入密码，最多录入三次，如果正确就结束循环
# else和for搭配使用
for item in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均输入错误')


# else和while搭配使用
a = 0
while a < 3:
    # 条件执行体
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
else:
    print('对不起，三次密码均输入错误')

