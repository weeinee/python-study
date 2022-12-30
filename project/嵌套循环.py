# 输出一个三行四列的矩形
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # print('*', end='')
        print(i, '*', j, '=', i*j, end='\t')
    print()
