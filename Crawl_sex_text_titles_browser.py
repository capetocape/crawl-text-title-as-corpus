#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
#伪装浏览器，获取url地址的源代码
def getHtml2(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
    wb_data = requests.get(url, headers=head,timeout=30)
    print (type(wb_data))
    soup = BeautifulSoup(wb_data.text.encode('ISO-8859-1'), 'lxml')
    print(type(soup))
    print ('\n')
    return soup

#从内容中提取所有图片的标题(针对：url1 = 'https://www.153ss.com/htm/piclist)
def extract_title_piclist(url,out):
    #获取url的源代码内容
    content = getHtml2(url)
    #一个列表
    content = content.find_all("li")
    #提取文本
    # 思路是利用str.index()和序列的切片
    try:
        for line in content:
            line = str(line)
            num1 = line.index('</span>',0)
            num2 = line.index('</a>',num1)
            title = line[(num1+7):num2]
            title = title.strip()
            out.write(title + '\n')
            print(title)
    except ValueError:
        print ('VauleError ...')
#将提取到的标题，写入到文件中

def write_file2(url,write_path):

    if os.path.exists(write_path):
        print ('remove :',write_path)
        os.remove(write_path)
    out = open(write_path,'a')
    for i in range(0,953):
        count = i + 1
        try:
            print ('===============')
            print ('count: ',count)
            url_piclist = url + str(count) + '.htm'
            print (url_piclist)
            extract_title_piclist(url_piclist,out)
            print ('===============')
        except:
            continue
    out.close()

if __name__ == '__main__':
    #302ss.com中piclist1,爬取页面数从1到953 
    url2 = 'https://www.302ss.com/htm/piclist1/'
    write_path2 = './sex_title/www_302ss_com_piclist1'
    write_file2(url2,write_path2)

