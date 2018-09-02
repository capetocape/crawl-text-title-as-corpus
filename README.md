# crawl-text-as-corpus
Crawling data from websites as text corpus  

自然语言处理——中文文本分类，需要文本语料库，这是一个从网站爬取标题文本的代码库

### 1.Crawl_sex_text_titles.py
该程序用来从网站‘http://www.mzitu.com/page/’ 爬取文本标题  

### 2.Crawl_sex_text_titles_browser.py
有些网站不让爬取数据，我们可以伪装浏览器爬取，该程序从以下网站伪装浏览器爬取文本标题：  
https://www.302ss.com/htm/piclist1  
  
下面提供一些网站，代码只要改一些细节就可以继续爬取了：  


### 3.title文件夹
  
该文件夹保存着我爬取的这些网站的文本数据。  
  
  
## 硬件及环境：  
**操作系统** Win7 |Python 3.5.2 |Anaconda 4.1.1 (64-bit)|  
urllib.request **version** = '3.5'  
bs4 **version** = '4.4.1'  
requests **version** = '2.14.2'
