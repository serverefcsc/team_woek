# requests模块
# -概念：python中原生的基于网络请求的模块。模拟浏览器进行请求发送，获取页面数据。
# - 安装：pip install requests

# 爬取搜狗首页的页面数据
# 1.指定url
# 2.基于requests模块的请求发送
# 3.获取响应对象中的数据值
# 4.持久化存储

import requests

# 1.
url = 'https://www.sogou.com/'

# 2.调用get方法，该方法就可以根据指定的url发起请求，返回一个响应对象
response = requests.get(url=url, proxies={'https': '121.139.218.165:31409'})

# 3.text属性就可以将响应对象中的数据值进行获取,text属性返回的数据类型是str
page_text = response.text

# print(page_text)
# 4.
with open('./sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    print('over')

# response.content #返回的是二进制的页面数据
# response.headers #返回的是响应头信息
# response.status_code
# response.url
# response.encoding #返回的是响应对象中存储数据的原始编码格式


# -----------------------------------------------------------------------------------------------------


# 爬取搜狗指定词条搜索后的页面数据
word = input('enter a word:')

url = 'https://www.sogou.com/web?'
# 如果url携带了参数，我们最好需要将参数封装到一个字典中
param = {
    'query': word
}
# 将封装好的参数作业到请求中
response = requests.get(url=url, params=param)

page_text = response.text

fileName = word + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)

# ----------------------------------------------------------------------------------------------------

# 需求：登录豆瓣电影，爬取登录成功后的页面数据

import requests

url = 'https://www.douban.com/accounts/login'

# 对post请求携带的参数进行字典封装
data = {
    "source": "index_nav",
    "form_email": "15027900535",
    "form_password": "bobo@15027900535",
}
response = requests.post(url=url, data=data)

page_text = response.text

with open('douban.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
    print('over')

# -------------------------------------------------------------------------------------------------------


# 爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据
import requests

url = 'https://movie.douban.com/j/chart/top_list?'

param = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "100",
    "limit": "20",
}
response = requests.get(url=url, params=param, proxies={'https': '121.139.218.165:31409'})

print(response.text)

# -------------------------------------------------------------------------------------------------------


# 需求：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据
import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
city = input('enter a city:')
data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": "2",
    "pageSize": "10",
}
response = requests.post(url=url, data=data)

# response.text


# --------------------------------------------------------------------------------------------------------


# 需求：爬取博客园指定页面下的页面数据
import requests
import os

url = 'https://www.cnblogs.com/#p'

# 新建一个文件夹
if not os.path.exists('boke'):
    os.mkdir('boke')

# 提供一组页码的范围
start_page = int(input('enter a start page:'))
end_page = int(input('enter a end page:'))

for page in range(start_page, end_page + 1):
    url = url + str(page)
    response = requests.get(url=url, proxies={'https': '121.139.218.165:31409'})
    page_text = response.text

    fileName = str(page) + ".html"
    filePath = './boke/' + fileName
    with open(filePath, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
        print('第%d页下载成功' % page)

# ----------------------------------------------------------------------------------------------------------


# 反爬机制：UA验证
# 反反爬机制：UA身份的伪装
# 流程：封装一个请求头字典（UA）。将该字典作用到请求对象中

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
city = input('enter a city:')
data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": "2",
    "pageSize": "10",
}
# 自制定请求头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
response = requests.post(url=url, data=data, headers=headers)

# response.text
