# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class SearchData:

    def __init__(self):
        print "SearchData-init"
        pass

    def search(self):
        print "start to search"
        f = open('data/getdatafromdb.txt', 'w')

        url = "http://movie.douban.com/subject/26277313/"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        ALL = soup.findAll(attrs = {'class': 'review-short'})

        number = 1

        for each in ALL:
            #title = each.find("a", attrs = {"title": True})
            if each.span.string:
                text = '\n' + str(number) + "." + each.span.string
                f.write(text)

            number += 1

        f.close()

