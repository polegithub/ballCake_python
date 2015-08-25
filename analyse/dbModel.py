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
    bookName = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    score = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    scoredNum =  Column(Integer)
    author = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    publisher = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    publishTime =  Column(Integer)
    price =Column(String(40,collation='utf8_unicode_ci'),nullable=True)

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(String(40,collation='utf8_unicode_ci'),nullable=True)

    def __init__(self,bookName,score,scoredNum,author,publisher,publishTime,price):
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
    firstRegion = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    director = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    dou_url =  Column(String(100,collation='utf8_unicode_ci'),nullable=True)

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(String(40,collation='utf8_unicode_ci'),nullable=True)

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
    movieId =   Column(Integer, nullable=False)
    movieName = Column(String(40,collation="utf8_unicode_ci"),nullable=True)
    movietag = Column(String(40,collation='utf8_unicode_ci'),nullable=True)
    tagIndex = Column(Integer,nullable = False)
    tagType = Column(Integer,nullable = False) # tag的类型，待定义

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(String(40,collation='utf8_unicode_ci'),nullable=True)

    def __init__(self,movieId,movieName,tag,index,type,
                 create_time,update_time):
        self.movieName = movieName
        self.movieId = movieId
        self.movietag = tag
        self.tagIndex = index
        self.tagType = type

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
    recommendMovieId =  Column(String(40),nullable=True)
    index =Column(Integer, nullable=False)

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(String(40,collation='utf8_unicode_ci'),nullable=True)

    def __init__(self, movieId, recommendMovieId,index,create_time, update_time):
        self.movieId = movieId
        # self.movieName = movieName
        self.recommendMovieId = recommendMovieId
        self.index  = index
        self.create_time = create_time
        self.update_time = update_time


    def __repr__(self):
        return '<movieId: %r>' % self.movieId


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
    update_time = Column(String(40,collation='utf8_unicode_ci'),nullable=True)

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
