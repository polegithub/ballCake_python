#coding = utf-8

__author__ = 'chengpoleness'


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from crawler.getBasicData.doubanMovie import *
from config.config import *

class Factory:

    def __init__(self):
        session = sessionmaker(bind=create_engine(engineBallRemout))
        self.session = session()

    def create_scrapy(self, name):
        if name == 'doubanMovie':
            d = DoubanMovie(self.session)
            d.startSearchMovie()
            pass
        else:
            print('enter else of create scrap')
        # if name == 'baidu':
        #     return baidu.BaiDu(self.session, start_id)
        # if name == 'eleme':
        #     return eleme.Eleme(self.session, start_id)

    def saveData(self):
        pass


