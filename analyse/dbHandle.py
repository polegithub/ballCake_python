__author__ = 'chengpoleness'

import MySQLdb
# -*- coding: utf-8 -*-

# polen MAC: mysql：  user="root",passwd=""
# chunke :mysql: you change it as your local computer

#localhost = 127.0.0.1


def do_init_db():

    conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="test",charset="utf8")
    curs = conn.cursor()

    try:
        curs.execute('create database sourceDataDB')
    except:
        print('addBallCakeDB exist!')


    conn.select_db('sourceDataDB')

    create a table named addfields
    try:
        curs.execute('create table addfields(id int PRIMARY KEY NOT NULL,name text)')
    except:
        print('The table addfields exists!')


    add the fileds
    try:
        for i in range(1):
            sql = "alter table addfields add key%s text" %i
            curs.execute(sql)
    except Exception,e:
        print e


    for i in range(4): #insert 5 lines
        sql = "insert into addfields set id=%s" %i
        curs.execute(sql)
        sql = "update addfields set name = 'hello%s' where id= %s"%(i,i)
        curs.execute(sql)
        # for j in range(5):
        #     sql = "update addfields set key%s = 'world%s%s' where id=%s"%(j,i,j,i)
        #     curs.execute(sql)

    #this is very important
    conn.commit()
    curs.close()
    conn.close()
