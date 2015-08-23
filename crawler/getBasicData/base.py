#-*- coding: UTF-8 -*-
__author__ = 'chengpoleness'



# import Geohash
import time

from sqlalchemy import and_
from bs4 import BeautifulSoup
# from lib.decorator import roll_back
#
from analyse.dbModel import MovieBasicInfo,MovieTagInfo,RecommendationMovieInfo,MovieScoreInfo

__metaclass__ = type


class Base:

    def __init__(self, session):
        self.session = session
        # self.proxy = self.__get_proxy()
        # self.proxy_count = len(self.proxy)


    # def __get_proxy(self):
    #     proxy = self.session.query(Proxy).filter_by(type='HTTP').all()
    #     return proxy


    #基本信息
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


    #电影标签
    def insert_Movie_tag(self,movieId,movieName,judgeTag1,judgeTag2,judgeTag3,judgeTag4,judgeTag5,
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


    # 同类推荐
    def insert_Movie_recommendMovieId(self,movieId,moviewNewId):
        movieNew = self.query_Movie_left_recommend_place(movieId)
        if movieNew is not  None:
            movieModel = RecommendationMovieInfo(movieNew = moviewNewId)
            self.session.add(movieModel)
            self.session.commit()


    def query_Movie_left_recommend_place(self,movieId):
        for i in range(1,10):
            index = str(i)
            movieNew = 'recommendMovie'+index
            result = self.session.query(RecommendationMovieInfo).movieNew.filter_by(movieId = movieId )
            if result is None:
                return movieNew

    #得分
    def insert_Movie_Score(self,movieId,movieName,totalScore,totalNum,
                          FiveScore,FourScore,ThreeScore,TwoScore,OneScore,):
        if self.query_Movie_Score_by_movieId(movieId) is None:
            movieModel = MovieScoreInfo(movieId = movieId,movieName = movieName,totalScore= totalScore,totalNum=totalNum,FiveScore= FiveScore,FourScore=FourScore,
                                        ThreeScore= ThreeScore,TwoScore=TwoScore,OneScore=OneScore,
                                        create_time=int(time.time()),update_time=int(time.time()))
            self.session.add(movieModel)
            self.session.commit()


    def query_Movie_Score_by_movieId(self,movieId):
        return self.session.query(MovieScoreInfo).filter_by(movieId = movieId).first()

