# 从键盘录入一个整数，编写程序让计算机判断奇偶性
num = int(input('请输入一个整数：'))
# 条件判断
if num % 2 == 0:
    print(num, '是偶数')
else:
    print(num, '是奇数')