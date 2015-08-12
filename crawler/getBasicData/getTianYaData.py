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

        for pagenum in range(1,3):        #从第1页爬到第x页(不包含最后一页)

            strpagenum = str(pagenum)      #页数的str表示

            txt ='data/tianya/ziZhiTongJian' + strpagenum
            f = open(txt,'w')

            print "Getting data for Page " + strpagenum   #shell里面显示的，表示已爬到多少页
            url = "http://bbs.tianya.cn/post-no05-51326-"+strpagenum + ".shtml" #网址
            page = urllib2.urlopen(url)     #打开网页
            soup = BeautifulSoup(page)      #用BeautifulSoup解析网页
             # print(soup)


            ALL = soup.findAll(attrs = {'class' : 'atl-item'})

            number =1


            for each in ALL :               #枚举所有的问题和回答

                if each:
                    title = ''
                    name = '未知'

                    titleInfo =each.find('strong',class_ = 'host')
                    if titleInfo:
                        title = titleInfo.text

                    nameInfo = each.find('div',class_ = 'atl-info')
                    if nameInfo:
                        name = nameInfo.find('a',class_ = 'js-vip-check').text
                    if name:
                        title ='\n' + strpagenum +'-' + str(number) +'楼 '+ title + ' ' + name +'\n'

                    f.write(title)

                    content = each.find('div', class_= 'bbs-content')

                    if content.text:
                         contentIndeed = ''.join(content.text.split('\t'))
                         contentIndeed = contentIndeed.replace(' ','\n')

                         f.write(contentIndeed)


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