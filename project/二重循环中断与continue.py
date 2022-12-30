# 二重循环中的break和continue用于控制本层循环
# continue
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()



# break
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            break
        print(j)