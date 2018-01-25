#encoding=utf-8

__author__ ='chp'

import urllib
import time
from pyquery import PyQuery as pq

#入口url
url = 'https://www.autohome.com.cn/car/'
#具体的车站型号入口url
pre_url = 'https://car.autohome.com.cn/pic/brand-'
post_url = '.html'
#请求
request = urllib.request.Request(url)
#返回结果
response = urllib.request.urlopen(request)
ret_content = response.read();
#设置解码方式
ret_content = ret_content.decode('gb2312', 'ignore')
#使用pyquwey进行解析
ret_content = pq(ret_content)
#筛选id为tab-content-item2的选项内容
ret_content = ret_content('#tab-content-item2')
doc = ret_content('#contentSeries')

for item in doc.items('dl'):
    time.sleep(6)
    if item.attr('data') == 'SR_Ht':
        continue
    for itemX in item('dd').items():
        time.sleep(6)
        print(itemX('a').attr('cname') + ' ' )
        brand_url = pre_url + itemX('a').attr('vos') + post_url
        request = urllib.request.Request(brand_url)
        ret_html = urllib.request.urlopen(request).read().decode('gb2312', 'ignore')
        ret_pq = pq(ret_html)('span')('.fn-left')
        for itemY in ret_pq.items():
            print(itemY('a').text())


#print(doc)