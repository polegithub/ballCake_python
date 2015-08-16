__author__ = 'chengpoleness'



# import Geohash
import time

from sqlalchemy import and_
from bs4 import BeautifulSoup
# from lib.decorator import roll_back
#
from analyse.dbModel import MovieBasicInfo,MovieTagInfo

__metaclass__ = type


class Base:

    def __init__(self, session):
        self.session = session
        # self.proxy = self.__get_proxy()
        # self.proxy_count = len(self.proxy)


    # def __get_proxy(self):
    #     proxy = self.session.query(Proxy).filter_by(type='HTTP').all()
    #     return proxy

    def insert_Moview_basic(self,movieId,movieName,score,scoredNum,type,year,firstRegion,director,url):

            if self.query_Movie_basic_by_movieId(movieId) is None:

                movieModel  = MovieBasicInfo(movieId = movieId,movieName = movieName,
                                             score =score,scoredNum =scoredNum,type =type,
                                             year = year,firstRegion = firstRegion,director=director,url=url,
                                             create_time=int(time.time()), update_time=int(time.time()))
                self.session.add(movieModel)
                self.session.commit()


    def query_Movie_basic_by_movieId(self, movieId):
        return self.session.query(MovieBasicInfo).filter_by(movieId=movieId).first()


    # @roll_back
    # def query_Movie_by_Tag(self, id,moviewId,tag,):
    #     return self.session.query(MovieBasicInfo).filter_by(movieid=moviewId).first()


    def insert_Moview_tag(self,movieId,movieName,judgeTag1,judgeTag2,judgeTag3,judgeTag4,judgeTag5,
                          typeTag1,typeTag2,typeTag3,typeTag4,typeTag5):

            if self.query_Movie_by_moviewId(movieId) is None:
                movieModel  = MovieTagInfo(movieId = movieId,movieName = movieName,
                                             judgeTag1 =judgeTag1,judgeTag2 =judgeTag2,judgeTag3 =judgeTag3,
                                             judgeTag4 =judgeTag4,judgeTag5 =judgeTag5,typeTag1 =typeTag1,
                                             typeTag2 =typeTag2,typeTag3 =typeTag3,typeTag4 =typeTag4,typeTag5 =typeTag5,
                                             create_time=int(time.time()), update_time=int(time.time()))
                self.session.add(movieModel)
                self.session.commit()

    def query_Movie_tag_by_movieId(self, movieId):
        return self.session.query(MovieTagInfo).filter_by(movieId=movieId).first()


    # @roll_back
