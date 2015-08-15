__author__ = 'chengpoleness'

#coding = utf-8


#coding = utf-8


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from crawler.getBasicData.doubanMovie import *
from config.config import *

class Factory:

    def __init__(self):
        session = sessionmaker(bind=create_engine(engineBall))
        self.session = session()

    def create_scrapy(self, name):
        # if name == 'baidu':
        #     return baidu.BaiDu(self.session, start_id)
        # if name == 'eleme':
        #     return eleme.Eleme(self.session, start_id)
        if name == 'douban_movie':
            d = DoubanMovie(self.session)
            d.startSearchMovie()
            pass

