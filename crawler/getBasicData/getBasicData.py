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
        f.write("No Answer")

        for pagenum in range(1,5):        #从第1页爬到第11页
             strpagenum = str(pagenum)      #页数的str表示
             print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
             url = "http://www.zhihu.com/collection/27109279?page="+strpagenum  #网址
             page = urllib2.urlopen(url)     #打开网页
             soup = BeautifulSoup(page)      #用BeautifulSoup解析网页

    #找到具有class属性为下面两个的所有Tag
        ALL = soup.findAll(attrs = {'class' : ['zm-item-title','zh-summary summary clearfix'] })
        for each in ALL :               #枚举所有的问题和回答
          #print type(each.string)
          #print each.name
            if each.name == 'h2' :      #如果Tag为h2类型，说明是问题
                #print each.a.string     #问题中还有一个<a..>，所以要each.a.string取出内容
                if (each.a and each.a.string) :       #如果非空，才能写入
                    each.a.string = each.a.string + '\n'
                    print each.a.string     #问题中还有一个<a..>，所以要each.a.string取出内容

                    f.write(each.a.string)
                else :                  #否则写"No Answer"
                    f.write("No Answer")
            else :                      #如果是回答，同样写入
                print each.string

                if each.string:
                    f.write(each.string)
                else :
                    f.write("No Answer")

        f.close()                           #关闭文件







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
