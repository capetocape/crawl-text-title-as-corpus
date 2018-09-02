#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from urllib.request import urlopen
#获取url地址的源代码
def getHtml(url):
    # 获取网页内容
    page = urlopen(url)
    html = str(page.read(),'utf-8')
    return html

#从内容中提取所有图片的标题(针对：url = 'http://www.mzitu.com/page/')
def extract_title_mzi(url,out):
    #获取url的源代码内容
    content = getHtml(url)
    #提取str1和str2中间的字符串
    str1 = '<div class="postlist">'
    str2 = '<div class="sidebar">'
    content = content.partition(str1)[2]
    content = content.partition(str2)[0]
    #提取文本
    beg = 0
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:
            num1 = content.index('alt=\'',beg)
            num2 = content.index('\' src=',num1)
            title = content[(num1+5):num2]
            title = title.strip()
            out.write(title + '\n')
            print(title)
            beg = num2
    except ValueError:
         return title_list

#将提取到的标题，写入到文件中
#路径:'./sex_title/'
def write_file1(url,write_path):
    if os.path.exists(write_path):
        os.remove(write_path)
    out = open(write_path,'a')
    for i in range(187):
        count = i + 1
        print ('count: ',count)
        print ('\n\n')
        url_mzi = url + str(count) + '/'
        extract_title_mzi(url_mzi,out)
    out.close()


if __name__ == '__main__':
    #mzitu网站，爬取该网站，页面数从1到187，爬取所有色情标题 
    url = 'http://www.mzitu.com/page/'
    write_path = './sex_title/www_mzitu_com'
    write_file1(url,write_path)
