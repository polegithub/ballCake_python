# encoding:utf-8
__author__ = 'chengpoleness'

from  sqlalchemy import create_engine
from  analyse.dbModel import Base
from  config.config import *

if __name__ == '__main__':
    #this py used for handle sqlalchemy,now just for create db
    e = create_engine(engineBallRemout)
    # e = create_engine(engineBallLocal)
    # Base.metadata.drop_all(e)
    Base.metadata.create_all(e)

