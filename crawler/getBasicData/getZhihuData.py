#coding=utf-8

import urllib2
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class SearchData:

    def __init__(self):
        print ('searchData-init')
        pass

    def search(self):
        print('start to search')
        f = open('data/howtoTucao.txt','w')     #打开文件#

        for pagenum in range(1,2):        #从第1页爬到第11页
             strpagenum = str(pagenum)      #页数的str表示
             print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
             url = "http://www.zhihu.com/collection/27109279?page="+strpagenum  #网址
             page = urllib2.urlopen(url)     #打开网页
             soup = BeautifulSoup(page)      #用BeautifulSoup解析网页
             # print(soup)


    #找到具有class属性为下面两个的所有Tag
        # ALL = soup.findAll(attrs = {'class' : ['zm-item-title','zh-summary summary clearfix'] })
        ALL = soup.findAll(attrs = {'class' : 'zm-item'})

        number =1;

        for each in ALL :               #枚举所有的问题和回答
            title = each.find(attrs = {'class':'zm-item-title'})
            if title:
                print('title:',title.text)
                text = '\n' + str(number) +'.'+ title.text
                f.write(text)

            answer = each.find(attrs = {'class':'zh-summary'})

            if answer:
                print('answer：', answer.text)
                f.write(answer.text)

            number = number+1


        f.close()                           #关闭文件


    def searchUrlByPage(self,url,pageMin,pageMax):
        if url:
            if pageMax>pageMin and pageMin>=0:
                for pagenum in range(pageMin,pageMax):
                    strpagenum = str(pagenum)      #页数的str表示
                    print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
                    url = url + strpagenum  #网址
                    page = urllib2.urlopen(url)     #打开网页
                    soup = BeautifulSoup(page)      #用BeautifulSoup解析网页

                    if soup:
                        return soup

        return None


# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

# //*[@id="q_banner_950_90_5"]

# def getContent(html):
#     # print(html)
#     # conent=  r'<div class="atl-item"(.*?)<div class'
#
#
#     # print(soup)
#     #
#     # content = r'<div class="atl-item".*<div class="alt-head"'
#     # content_re = re.compile(content, re.M)
#     # result = content_re.findall(html)
#     #
#     # result=re.findall(content,html,re.M)
#     soup = BeautifulSoup(html)
#     # sub =soup.findAll('div','js_username')
#     atl_items = soup.find_all('div',class_='atl-item')
#
#     for item in atl_items:
#         try:
#
#             js_username = item['js_username']
#             bbs_content = item.find('div', class_='bbs-content')
#             print(js_username)
#             print('\n\n')
#             print bbs_content.text
#         except Exception:
#             pass
#     # print(len(atl_items))
#     # return sub
#
# # //*[@id="1"]
# # def getImg(html):
#     # reg = r'src="(.+?\.jpg)" pic_ext'
#     # imgre = re.compile(reg)
#     # imglist = re.findall(imgre,html)
#     # x = 0
#     # for imgurl in imglist:
#     #     urllib.urlretrieve(imgurl,'%s.jpg' % x)
#     #     x+=1
#
#
# html = getHtml("http://bbs.tianya.cn/post-no05-51326-1.shtml")
#
# print getContent(html)
