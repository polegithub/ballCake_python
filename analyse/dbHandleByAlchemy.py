# encoding:utf-8
__author__ = 'chengpoleness'

from  sqlalchemy import create_engine
from  analyse.dbModel import Base
from  config.config import *

if __name__ == '__main__':
    #this py used for handle sqlalchemy,now just for create db
    e = create_engine(engineBallRemout)
<<<<<<< HEAD
    #e = create_engine(engineBall)
    Base.metadata.drop_all(e)
=======
    # e = create_engine(engineBallLocal)
    # Base.metadata.drop_all(e)
>>>>>>> 33f5e17c4929bcc28f2b2fc74563766f44865491
    Base.metadata.create_all(e)

