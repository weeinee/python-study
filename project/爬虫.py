# 1.获取资源  -->抓一个数据包 时间长
# 2.发送请求
# 3.解析数据
# 4.保存数据
import parsel
import requests

# 获取数据
# 分析数据来源 抓包（只要抓包抓得好，没有爬虫爬不了）
# 分析网页性质：右键+查看网页源代码
# 静态数据：能搜到 就不需要抓包 直接以浏览器地址导航栏的连接作为数据包的链接就可以
# 动态数据：分析 开发者工具（抓包）
# url 变量名

url = 'https://www.bbiquge.net/book/37325/14387340.html'
# 发送请求

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.42 '
}
# 开发者工具 浏览器自带 network 网络面板 f12
# set 集合 数据容器 去重{‘1’，1}
# items 类字典 dict{'':''}

response = requests.get(url=url, headers=headers)

# get请求不改变数据 主要用于下载
# post多用于上传 要改变数据
# 浏览器不能直接打开post请求
# <Response [200]> ————>响应体对象 [200-299]请求成功

print(response.text)
print(response.headers)
#parsel不能直接对获取到的文本数据做解析-->转对象
selector=parsel.Selector(response.text)
selector.
