#coding=utf-8
import urllib
import re
from bs4 import BeautifulSoup



def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# //*[@id="q_banner_950_90_5"]

def getContent(html):
    # print(html)
    # conent=  r'<div class="atl-item"(.*?)<div class'


    # print(soup)
    #
    # content = r'<div class="atl-item".*<div class="alt-head"'
    # content_re = re.compile(content, re.M)
    # result = content_re.findall(html)
    #
    # result=re.findall(content,html,re.M)
    soup = BeautifulSoup(html)
    # sub =soup.findAll('div','js_username')
    atl_items = soup.find_all('div',class_='atl-item')

    for item in atl_items:
        try:

            js_username = item['js_username']
            bbs_content = item.find('div', class_='bbs-content')
            print(js_username)
            print('\n\n')
            print bbs_content.text
        except Exception:
            pass
    # print(len(atl_items))
    # return sub

# //*[@id="1"]
# def getImg(html):
    # reg = r'src="(.+?\.jpg)" pic_ext'
    # imgre = re.compile(reg)
    # imglist = re.findall(imgre,html)
    # x = 0
    # for imgurl in imglist:
    #     urllib.urlretrieve(imgurl,'%s.jpg' % x)
    #     x+=1


html = getHtml("http://bbs.tianya.cn/post-no05-51326-1.shtml")

print getContent(html)
