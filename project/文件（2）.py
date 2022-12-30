"""
文件的打开模式
r   只读模式打开
rb  只读模式打开二进制文件 如图片文件
w   覆盖写模式 文件不存在就创建 文件存在就内容覆盖
wb  覆盖写入二进制数据 文件不存在就创建 文件存在就覆盖
a   追加写模式 文件不存在创建 文件存在 在文件最后追加内容
+   与w/r/a等一同使用，在原功能的基础上增加同时读写功能

file.read(size)     从文件中读取size个字符或字节 如果没有给定参数就全部读取         
file.readline(size) 读取文件中的一行数据，如果给定参数，则读取文件中的size个字符或字节
file.readlines()    从文件中读取所有内容，结果为列表类型
file.write(s)       将字符s写入文件
file.writelines(lst)将内容全部为字符串列表lst写入文件
file.seek(offset)   改变当前文件操作指针的位置，英文占一个字节，中文gbk编码占两个字节，utf-8编码占三个字节

"""
def my_write(s):
    # 打开文件
    file=open('b.txt','a',encoding='utf-8')
    # 写入内容
    file.write(s)
    file.write('\n')
    file.close()

#调用两次
my_write('伟大中国梦')
my_write('北京欢迎你')




