__author__ = 'chengpoleness'


from  sqlalchemy import Column,String,create_engine
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base

from config.config import *

Base  = declarative_base()


    # def __init__(self,session,BookId,name,score,scoredNum,author,publisher,pubslishTime,price):
    #
    #
    # def addBookBasicInfo():
    #     newBook = Booker(id = BookId,bookName = name,score =score,scoredNum = scoredNum,author = author)
    #     sessionAddHandle(newBook,session)
    #
    #
    # def createDoubanSession():
    #     engine = create_engine(engineBall)
    #     DBSession = sessionmaker(bind=engine)
    #     session = DBSession()
    #     return session
    #
    #
    # def sessionFinish(session):
    #     session.commit()
    #     session.close()
    #
    # def sessionAddHandle(user,session):
    #     session.add(user)
    #     sessionFinish(session)