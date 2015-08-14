__author__ = 'chengpoleness'




import MySQLdb
# -*- coding: utf-8 -*-

#localhost = 127.0.0.1


def do_init_db(dbType):

    conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="mysql",charset="utf8")
    curs = conn.cursor()

    try:
        curs.execute('create database if not exist ballCake')
    except:
        print('addBallCakeDB success!')


    conn.select_db('ballCake')

    # n = curs.execute("select * from user")
    # for row in curs.fetchall():
    #     print row
    #     for r in row:
    #         print r

    # create a table named addfields
    if dbType == 'douban':
        try:
                curs.execute('create table douban_book(id int PRIMARY KEY NOT NULL,bookName text,score text,scoedNum int)')
        except:
                print('The table douban_book success!')

        try:
                # sql = "alter table douban_book add (publisher text,author text,publishTime text,price text)"
                sql = "alter table douban_book add (price text)"
                curs.execute(sql)
        except:
                print('add keys for douban')



    # add the fileds
    # try:
    #     for i in range(1):
    #         sql = "alter table douba_book add key%s text" %i
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




