__author__ = 'chengpoleness'




import MySQLdb
# -*- coding: utf-8 -*-

#localhost = 127.0.0.1


def do_init_db():

    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="ballCake",charset="utf8")
    curs = conn.cursor()

    # try:
    #     curs.execute('create database sourceDataDB')
    # except:
    #     print('addBallCakeDB success!')
    #
    #
    # conn.select_db('sourceDataDB')
    #
    # # n = curs.execute("select * from user")
    # # for row in curs.fetchall():
    # #     print row
    # #     for r in row:
    # #         print r
    #
    # # create a table named addfields
    # try:
    #     curs.execute('create table addfields(id int PRIMARY KEY NOT NULL,name text)')
    # except:
    #     print('The table addfields success!')
    #
    #
    # # add the fileds
    # try:
    #     for i in range(1):
    #         sql = "alter table addfields add key%s text" %i
    #         curs.execute(sql)
    # except Exception,e:
    #     print e


    # for i in range(4): #insert 5 lines
    #     sql = "insert into addfields set id=%s" %i
    #     curs.execute(sql)
    #     sql = "update addfields set name = 'hello%s' where id= %s"%(i,i)
    #     curs.execute(sql)
    #     for j in range(5):
    #         sql = "update addfields set key%s = 'world%s%s' where id=%s"%(j,i,j,i)
    #         curs.execute(sql)

    #this is very important
    conn.commit()
    curs.close()
    conn.close()
