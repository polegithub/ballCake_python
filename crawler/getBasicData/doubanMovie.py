#-*- coding: UTF-8 -*-

import sys
import time
import urllib
import urllib2
import requests
import numpy as np
from bs4 import BeautifulSoup
from openpyxl import Workbook
from crawler.directory.directoryManager import contentClass

from crawler.directory.directoryManager import contentClass

reload(sys)
sys.setdefaultencoding('utf8')



class DoubanMovie():
    def __init__(self, session, start_id=1):
        self.session = session
        self.type = 2


    def startSearchMovie(self):
        #movie_tag_lists = ['爱情','喜剧','动画','科幻','剧情','动作']
        #movie_tag_lists = ['经典','悬疑','青春','犯罪','惊悚','文艺','纪录片']
        #movie_tag_lists=['励志','搞笑','恐怖','战争','短片','魔幻','传记']
        movie_tag_lists = ['经典']
        movie_lists = self.do_spider(movie_tag_lists)
        self.print_movie_lists_excel(movie_lists,movie_tag_lists)

    def do_spider(self,movie_tag_lists):
        movie_lists=[]
        for movie_tag in movie_tag_lists:
            movie_list = self.movie_spider(movie_tag)
            movie_list = sorted(movie_list,key=lambda x:x[1],reverse=True)
            movie_lists.append(movie_list)
        return movie_lists


    def movie_spider(self,movie_tag):
        page_num=0
        count=1
        movie_list=[]
        try_times=0

        #Some User Agents
        hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
             {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
             {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

        while(page_num < 2):
            url="http://www.douban.com/tag/"+urllib.quote(movie_tag)+"/movie?start="+str(page_num*15)
            time.sleep(np.random.rand()*2)

            #Last Version
            try:
                req = urllib2.Request(url, headers=hds[page_num%len(hds)])
                source_code = urllib2.urlopen(req).read()
                plain_text=str(source_code)
            except (urllib2.HTTPError, urllib2.URLError), e:
                print e
                continue

            ##Previous Version, IP is easy to be Forbidden
            #source_code = requests.get(url)
            #plain_text = source_code.text

            soup = BeautifulSoup(plain_text)
            list_soup = soup.find('div', {'class': 'mod movie-list'})

            try_times+=1
            if list_soup==None and try_times<200:
                continue
            elif list_soup==None or len(list_soup)<=1:
                break # Break when no informatoin got after 200 times requesting

            for movie_info in list_soup.findAll('dd'):
                titleFull =movie_info.find('a', {'class':'title'})

                title = titleFull.string.strip()

                url = titleFull.get('href')

                time.sleep(np.random.rand()*2)

                try:
                    req_detail = urllib2.Request(url)
                    source_code_detail = urllib2.urlopen(req_detail).read()
                    plain_text_detail=str(source_code_detail)
                except (urllib2.HTTPError, urllib2.URLError), e:
                    print e

                soup_detail = BeautifulSoup(plain_text_detail)


                try:
                    director = soup_detail.find("a",attrs = {"rel":"v:directedBy"}).string.strip()
                except:
                    director = "暂无"

                try:
                    actors = soup_detail.findAll("a",attrs = {"rel":"v:starring"})
                    actor_list = []
                    for i in range(0,len(actors)):
                        actor = actors[i].string.strip()
                        actor_list.append(actor)
                    actor = '/'.join(actor_list)
                except:
                    actor = "暂无"

                try:
                    type_lists = soup_detail.findAll("span",attrs = {"property":"v:genre"})
                    type_list = []
                    for i in range(0,len(type_lists)):
                        type = type_lists[i].string.strip()
                        type_list.append(type)
                    type = '/'.join(type_list)
                except:
                    type = "暂无"

                try:
                    ReleaseDate = soup_detail.find("span",attrs = {"property":"v:initialReleaseDate"}).string.strip()
                except:
                    ReleaseDate = "暂无"

                try:
                    rating_num = soup_detail.find("strong",attrs = {"property":"v:average"}).string.strip()
                except:
                    rating_num = "暂无"

                try:
                    vote_num = soup_detail.find("span",attrs = {"property":"v:votes"}).string.strip()
                except:
                    vote_num = "暂无"

                movie_model =[title,rating_num,vote_num,type,ReleaseDate,director,actor]

                movie_list.append(movie_model)
                try_times=0 #set 0 when got valid information
            page_num += 1
            print "Downloading Information From Page %d" % page_num
        return movie_list


    def print_movie_lists_excel(movie_lists,movie_tag_lists):
        wb=Workbook(optimized_write=True)
        ws=[]
        for i in range(len(movie_tag_lists)):
            ws.append(wb.create_sheet(title=movie_tag_lists[i].decode())) #utf8->unicode
        for i in range(len(movie_tag_lists)):
            ws[i].append(['序号','电影名','评分','评价人数','类型','年份','导演','演员'])
            count=1
            for bl in movie_lists[i]:
                ws[i].append([count,bl[0],float(bl[1]),int(bl[2]),bl[3],int(bl[4]),bl[5],bl[6]])
                count+=1


            # 获取 存储路径
        f =  contentClass()
        save_path= f.getContentForDouBan(2)
        print('save path:',save_path)


        for i in range(len(movie_tag_lists)):
            save_path+=('-'+movie_tag_lists[i].decode())
        save_path+='.xlsx'
        wb.save(save_path)



