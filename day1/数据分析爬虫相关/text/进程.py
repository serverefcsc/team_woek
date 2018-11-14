from multiprocessing import Process
from Team_Test.day1.数据分析爬虫相关 import cal_time
import requests


def get_page(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))

@cal_time
def main():
    p_list = []
    for i in ['https://www.python.org/', 'https://www.yahoo.com/', 'https://github.com/']:
        p = Process(target=get_page,args=(i,))
        p_list.append(p)
        p.start()
    for i in p_list:
        i.join()


main()
