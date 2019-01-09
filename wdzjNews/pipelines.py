# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class WdzjnewsPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect( host="localhost", user="root", password="", db="pythontest", port=3306 )

    def mysqlCreatTable(self):
        db = pymysql.connect( host="localhost", user="root", password="", db="pythontest", port=3306 )
        cursor = db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS wdzj_newsList (
                news_subMessage VARCHAR(999) ,
                news_source VARCHAR(90) ,
                news_time VARCHAR(666) ,
                news_title VARCHAR(666) )"""
        cursor.execute(sql)
        db.close()


    def insertMysql(self,item):
        db = pymysql.connect( host="localhost", user="root", password="", db="pythontest", port=3306 )
        cursor = db.cursor()
        sql = "insert into wdzj_newsList (news_title,\
        news_time,news_subMessage,news_source) \
        VALUES ('%s','%s','%s','%s')" % (
        item['news_title'], item['news_time'], item['news_subMessage'], item['news_source'])
        try:
            db.ping(reconnect=True)
            cursor.execute( sql )
            print( 'success--insert' )
            db.commit()
        except:
            db.rollback()
            print( 'error-----error' )

        db.close()


    def process_item(self, item, spider):

        self.mysqlCreatTable()
        self.insertMysql(item)

        return item
