'''会员  >=200 8折
        >100 9折
        <100 不打折
    非会员  >=200 95折
           <200 不打折'''
answer = input('你是会员吗？y/n：')
money = float(input('请输入您的购物金额：'))

# 外层判断是否是会员
if answer == 'y':
    print('是会员')
    if money >= 200:
        money *= 0.8
        print('最终金额：', money)
    elif 200 > money >= 100:
        money *= 0.9
        print('最终金额：', money)
    else:
        print('最终金额：', money)
else:  # 非会员
    print('不是会员')
    if money >= 200:
        money *= 0.95
        print('最终金额：', money)
    else:
        print('最终金额', money)