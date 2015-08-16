#coding = utf-8
__author__ = 'chengpoleness'


import time
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


from config.config import *

Base = declarative_base()


class Booker(Base):

    __tablename__ = table_DB_book

    id = Column(String(),primary_key=True)
    bookName = Column(String())
    score = Column(String())
    scoredNum = Column(int())
    author = Column(String())
    publisher = Column(String())
    publishTime = Column(String())
    price = Column(String())
    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self,id,bookName,score,scoredNum,author,publisher,publishTime,price):
        self.id = id
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

    id = Column(Integer, primary_key=True, nullable=False)
    movieId = Column(Integer, primary_key=True, nullable=False)
    movieName = Column(String(collation="utf8_unicode_ci"), nullable=False)
    score = Column(float,default=0)
    scoredNumber = Column(Integer, nullable=True)
    type = Column(String(collation='utf8_unicode_ci'),nullable=False)
    year = Column(String(collation='utf8_unicode_ci'),nullable=False)
    director = Column(String(collation='utf8_unicode_ci'),nullable=False)
    dou_url =  Column(String(collation='utf8_unicode_ci'),nullable=False)

    create_time = Column(Integer, default=int(time.time()))
    update_time = Column(Integer, default=int(time.time()))

    def __init__(self,id,movieId,movieName,score,scoredNum,type,year,director,url):
        self.id = id
        self.movieName = movieName
        self.score = score
        self.scoredNumber = scoredNum
        self.type = type
        self.year = year
        self.director = director
        self.dou_url = url

    def __repr__(self):
        return '<movieName: %r>' %self.movieName

# 序号','电影名',标签
class MovieTagInfo(Base):
    __tablename__ = table_DB_movie_basic

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

    def __init__(self,id,movieId,movieName,judgeTag1,judgeTag2,judgeTag3,judgeTag4,judgeTag5,typeTag1,typeTag2,typeTag3,typeTag4,typeTag5):
        self.id = id
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


    def __repr__(self):
        return '<movieName: %r>' %self.movieName


#同类影片 - chunke建一下

#评分建表 id,moviewId,totalScore,totalNum,FiveScore,FourScore,ThreeScore,TwoScore,OneScore
