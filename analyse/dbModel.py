#-*- coding: UTF-8 -*-

import time
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


from config.config import *

Base = declarative_base()


class Booker(Base):

    __tablename__ = table_DB_book

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    bookName = Column(String())
    score = Column(String())
    scoredNum =  Column(Integer)
    author = Column(String())
    publisher = Column(String())
    publishTime = Column(String())
    price = Column(String())
    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self,id,bookName,score,scoredNum,author,publisher,publishTime,price):
        self.bookName = bookName
        self.score = score
        self.scoredNum = scoredNum
        self.author = author
        self.publisher = publisher
        self.publishTime = publishTime
        self.price = price


    def __repr__(self):
        return '<bookName: %r>' % self.bookName


 # 序号','电影名','评分','评价人数','类型','年份','导演',‘豆瓣链接’
class MovieBasicInfo(Base):
    __tablename__ = table_DB_movie_basic

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    movieId = Column(Integer, primary_key=True, nullable=False)
    movieName = Column(String(collation="utf8_unicode_ci"), nullable=False)
    score = Column(Float,default=0)
    scoredCount = Column(Integer, nullable=True)
    movieType = Column(String(collation='utf8_unicode_ci'),nullable=False)
    releaseYear = Column(String(collation='utf8_unicode_ci'),nullable=False)
    director = Column(String(collation='utf8_unicode_ci'),nullable=False)
    dou_url =  Column(String(collation='utf8_unicode_ci'),nullable=False)

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self,movieId,movieName,score,scoredNum,type,year,firstRegion,director,url,create_time,update_time):
        self.movieName = movieName
        self.movieId = movieId
        self.score = score
        self.scoredCount = scoredNum
        self.movieType = type
        self.releaseYear = year
        self.firstRegion =firstRegion
        self.director = director
        self.dou_url = url
        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieName: %r>' %self.movieName

# 序号','电影名',标签
class MovieTagInfo(Base):
    __tablename__ = table_DB_movie_tag

    id =        Column(Integer, primary_key=True, nullable=False)
    movieId =   Column(Integer, primary_key=True, nullable=False)
    movieName = Column(String(collation="utf8_unicode_ci"),nullable=False)
    judgeTag1 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    judgeTag2 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    judgeTag3 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    judgeTag4 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    judgeTag5 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    typeTag1 =  Column(String(collation='utf8_unicode_ci'),nullable=False)
    typeTag2 =  Column(String(collation='utf8_unicode_ci'),nullable=False)
    typeTag3 =  Column(String(collation='utf8_unicode_ci'),nullable=False)
    typeTag4 =  Column(String(collation='utf8_unicode_ci'),nullable=False)
    typeTag5 =  Column(String(collation='utf8_unicode_ci'),nullable=False)



    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self,movieId,movieName,judgeTag1,judgeTag2,judgeTag3,judgeTag4,
                 judgeTag5,
                 typeTag1,typeTag2,typeTag3,typeTag4,typeTag5,
                 create_time,update_time):
        self.movieName = movieName
        self.movieId = movieId
        self.judgeTag1 = judgeTag1
        self.judgeTag2 = judgeTag2
        self.judegTag3 = judgeTag3
        self.judgeTag4 = judgeTag4
        self.judgeTag5 = judgeTag5

        self.typeTag1 = typeTag1
        self.typeTag2 = typeTag2
        self.typeTag3 = typeTag3
        self.typeTag4 = typeTag4
        self.typeTag5 = typeTag5

        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieName: %r>' %self.movieName


#同类影片 - chunke建一下
#'序号', '电影名', '推荐电影'
class RecommendationMovieInfo(Base):
    __tablename__ = table_DB_recommendation_movie

    id = Column(Integer, primary_key=True, nullable=False)
    movieId = Column(Integer, primary_key=True, nullable=False)
    movieName = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie1 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie2 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie3 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie4 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie5 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie6 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie7 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie8 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie9 = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendationmovie10 = Column(String(collation='utf8_unicode_ci'),nullable=False)



    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

#多行对齐还没有做好
    def __init__(self, movieId, movieName, recommendationmovie1, recommendationmovie2, recommendationmovie3, recommendationmovie4, recommendationmovie5, recommendationmovie6, recommendationmovie7, recommendationmovie8, recommendationmovie9, recommendationmovie10, create_time, update_time):
        self.movieId = movieId
        self.movieName = movieName
        self.recommendationmovie1 = recommendationmovie1
        self.recommendationmovie2 = recommendationmovie2
        self.recommendationmovie3 = recommendationmovie3
        self.recommendationmovie4 = recommendationmovie4
        self.recommendationmovie5 = recommendationmovie5
        self.recommendationmovie6 = recommendationmovie6
        self.recommendationmovie7 = recommendationmovie7
        self.recommendationmovie8 = recommendationmovie8
        self.recommendationmovie9 = recommendationmovie9
        self.recommendationmovie10 = recommendationmovie10

        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieName: %r>' % self.movieName


#评分建表 id,moviewId,totalScore,totalNum,FiveScore,FourScore,ThreeScore,TwoScore,OneScore
#'序号', '电影名', '评分'
class MovieScoreInfo(Base):
    __tablename__ = table_DB_movie_score

    id = Column(Integer, primary_key = True, nullable = False)
    movieId = Column(Integer, primary_key = True, nullable = False)
    movieName = Column(String(collation='utf8_unicode_ci'),nullable=False)
    totalScore = Column(Float, default = 0)
    totalNum = Column(Integer, nullable = True)
    FiveScore = Column(String(collation='utf8_unicode_ci'),nullable=True)
    FourScore = Column(String(collation='utf8_unicode_ci'),nullable=True)
    ThreeScore = Column(String(collation='utf8_unicode_ci'),nullable=True)
    TwoScore = Column(String(collation='utf8_unicode_ci'),nullable=True)
    OneScore = Column(String(collation='utf8_unicode_ci'),nullable=True)


    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self, movieId, movieName, totalScore, totalNum, FiveScore, FourScore, ThreeScore, TwoScore, OneScore, create_time, update_time):
        self.movieId = movieId
        self.movieName = movieName
        self.totalScore = totalScore
        self.totalNum = totalNum
        self.FiveScore = FiveScore
        self.FourScore = FourScore
        self.ThreeScore = ThreeScore
        self.TwoScore = TwoScore
        self.OneScore = OneScore

        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieName: %r>' % self.movieName
