'''
文件的基本操作
  创建（打开）文件
    变量名=open（filename，mode，encoding）
  操作文件
    变量名.read（）
    变量名.write（s）
  关闭文件
    变量名.close（）

'''


def my_write():
    # 创建（打开）文件
    file = open('a.txt', 'w', encoding='utf-8')  # w是write 写
    # 操作
    file.write('伟大的中国梦')
    # 关闭
    file.close()



#读文件
def my_read():
    #打开文件
    file=open('a.txt','r',encoding='utf-8')
    #操作文件
    s=file.read()
    print(s)
    #关闭
    file.close()

#调用
my_read()

