from threading import Thread
import requests
from Team_Test.day1.数据分析爬虫相关 import cal_time

def get_page(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))

@cal_time
def main():
    t = []
    for i in ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com/']:
        th = Thread(target=get_page, args=(i,))
        t.append(th)
        th.start()
    for i in t:
        i.join()

main()
