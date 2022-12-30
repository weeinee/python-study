lst = []
for i in range(5):
    goods = input('请输入商品的编号和名称进行商品入库，每次只能输入一件')
    lst.append(goods)
# 输入所有的商品信息
for item in lst:
    print(item)

# 创建一个列表,用于存储购物车内的商品
cart = []
while True:
    flag = False
    num = input('请输入要购买的商品编号：')
    # 遍历商品列表查询商品是否存在
    for item in lst:
        if num == item[0:4]:
            flag = True
            cart.append(item)
            print('商品已成功添加到购物车')
            break
    if not flag and num != 'q':
        # if flag == False and num != 'q':
        print('商品不存在')

    if num == 'q':
        break
print("您购物车内已选择的商品为：")
# 反向
cart.reverse()
for item in cart:
    print(item)
