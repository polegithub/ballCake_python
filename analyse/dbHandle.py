__author__ = 'chengpoleness'


# -*- coding: utf-8 -*-


import MySQLdb

#localhost = 127.0.0.1

conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="ballCake",charset="utf8")
curs = conn.cursor()

def do_init_db(dbType):

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
    connectionEnd()


def connectionEnd():
    conn.commit()
    curs.close()
    conn.close()


def saveDataForDouban(id,bookName,score,scoredNum,author,publisher,publishTime,price):

    print('enter database handle')

    valuesName = (int(id),str(bookName),str(score),int(scoredNum),str(author))

    result = curs.execute('select * from douban_book where id = %d'%id)
    if result is not None:
        sqlName = "insert into douban_book (id,bookName,score,scoredNum,author) values ('%d','%s','%s','%d','%s')"%valuesName
    else:
        sqlName = "insert into douban_book (id,bookName,score,scoredNum,author) values ('%d','%s','%s','%d','%s')"%valuesName

    print(sqlName)

    curs.execute(sqlName)

    valuesPublish = (int(id),str(publisher),str(publishTime),str(price))
    sqlPublish = "insert into douban_book (id,publisher,publishTime,price) values ('%d','%s','%s','%s','%s')"%valuesPublish

    print(sqlPublish)

    curs.execute(sqlPublish)
    # sql = "insert into douban_book (id,bookName,score,scoredNum,author,publisher,publishTime,price) values ('2','2','9.7','0','2Randal E.Bryant / David O Hallaron ' ,'22', '2011-1-1' ,' 99.00')"

    # curs.execute(sql)


    # value =(int(id),str(bookName))
    # sql = "insert into douban_book (id,bookName,) values (%d,%s)"%(id,bookName)

    # curs.execute(sql)



    connectionEnd()



