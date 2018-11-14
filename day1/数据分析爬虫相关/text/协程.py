from gevent import monkey;monkey.patch_all()
import gevent
import requests
from Team_Test.day1.数据分析爬虫相关 import cal_time
def get_page(url):
    print('GET: %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' %(len(response.text),url))


@cal_time
def main():
    gevent.joinall([
        gevent.spawn(get_page,'https://www.python.org/'),
        gevent.spawn(get_page,'https://www.yahoo.com/'),
        gevent.spawn(get_page,'https://github.com/'),
    ])

main()


