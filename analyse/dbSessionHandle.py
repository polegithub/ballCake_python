__author__ = 'chengpoleness'


from  sqlalchemy import Column,String,create_engine
from  sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base

from config.config import *

Base  = declarative_base()

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


def addBookBasicInfo(session,BookId,name,score,scoredNum,author):
    newBook = Booker(id = BookId,bookName = name,score =score,scoredNum = scoredNum,author = author)
    sessionAddHandle(newBook,session)


def createDoubanSession():
    engine = create_engine(engineDouban)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def sessionFinish(session):
    session.commit()
    session.close()

def sessionAddHandle(user,session):
    session.add(user)
    sessionFinish(session)