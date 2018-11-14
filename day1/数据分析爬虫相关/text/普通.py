import requests
from Team_Test.day1.数据分析爬虫相关 import cal_time
def get_page(url):
    print('GET: %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' %(len(response.text),url))

@cal_time
def main():
    for i in ['https://www.python.org/','https://www.yahoo.com/','https://github.com/']:
        get_page(i)



if __name__ == '__main__':
    main()





"""
/Users/wangjifei/anaconda3/lib/
/usr/bin/python
/System/Library/Frameworks/Python.framework/Versions/
/usr/local/bin/
"""