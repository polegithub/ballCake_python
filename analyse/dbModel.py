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
    movieName = Column(String(40,collation="utf8_unicode_ci"), nullable=True)
    score = Column(Float,default=0)
    scoredCount = Column(Integer, nullable=True)
    movieType = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    releaseYear = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    director = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    dou_url =  Column(String(100,collation='utf8_unicode_ci'),nullable=True)

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
    movieName = Column(String(40,collation="utf8_unicode_ci"),nullable=True)
    judgeTag1 = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    judgeTag2 = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    judgeTag3 = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    judgeTag4 = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    judgeTag5 = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    typeTag1 =  Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    typeTag2 =  Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    typeTag3 =  Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    typeTag4 =  Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    typeTag5 =  Column(String(40,collation='utf8_unicode_ci'),nullable=True)



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


#'序号', '电影名', '推荐电影'
class RecommendationMovieInfo(Base):
    __tablename__ = table_DB_movie_similar

    id = Column(Integer, primary_key=True, nullable=False)
    movieId = Column(Integer, primary_key=True, nullable=False)
    # movieName = Column(String(collation='utf8_unicode_ci'),nullable=False)
    recommendMovie1 =  Column(String(40),nullable=True)
    recommendMovie2 =  Column(String(40),nullable=True)
    recommendMovie3 =  Column(String(40),nullable=True)
    recommendMovie4 =  Column(String(40),nullable=True)
    recommendMovie5 =  Column(String(40),nullable=True)
    recommendMovie6 =  Column(String(40),nullable=True)
    recommendMovie7 =  Column(String(40),nullable=True)
    recommendMovie8 =  Column(String(40),nullable=True)
    recommendMovie9 =  Column(String(40),nullable=True)
    recommendMovie10 = Column(String(40),nullable=True)



    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

#多行对齐还没有做好
    def __init__(self, movieId, movieId1, movieId2, movieId3, movieId4, movieId5,
                 movieId6, movieId7, movieId8, movieId9, movieId10, create_time, update_time):
        self.movieId = movieId
        # self.movieName = movieName
        self.recommendMovie1 = movieId1
        self.recommendMovie2 = movieId2
        self.recommendMovie3 = movieId3
        self.recommendMovie4 = movieId4
        self.recommendMovie5 = movieId5
        self.recommendMovie6 = movieId6
        self.recommendMovie7 = movieId7
        self.recommendMovie8 = movieId8
        self.recommendMovie9 = movieId9
        self.recommendMovie10 = movieId10

        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieName: %r>' % self.movieId


#评分建表 id,moviewId,totalScore,totalNum,FiveScore,FourScore,ThreeScore,TwoScore,OneScore
'序号', '电影名', '评分'
class MovieScoreInfo(Base):
    __tablename__ = table_DB_movie_score

    id = Column(Integer, primary_key = True, nullable = False)
    movieId = Column(Integer, primary_key = True, nullable = False)
    movieName = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    totalScore = Column(Float, default = 0)
    totalNum = Column(Integer, nullable = True)
    FiveScore = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    FourScore = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    ThreeScore = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    TwoScore = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    OneScore = Column(String(40,collation='utf8_unicode_ci'),nullable=True)


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
