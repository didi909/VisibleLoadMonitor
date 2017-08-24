# -*- coding: utf-8 -*-
#__author__="ZJL"

from flask import Flask
from flask import request
from flask import Response
import pymysql
import configparser
import pymysql
import json
import time
import datetime
import random


#读取数据库配置文件
db = configparser.ConfigParser()
db.read('conf/database.conf')

host=db.get('db', 'host')
port=db.get('db', 'port')
user=db.get('db', 'user')
passwd=db.get('db', 'pass')
dbname=db.get('db', 'dbname')

# host=db.get('db1', 'host')
# port=db.get('db1', 'port')
# user=db.get('db1', 'user')
# passwd=db.get('db1', 'pass')
# dbname=db.get('db1', 'dbname')

rowData = {}
data = []

# def randomData():
#
#     oneSec = datetime.timedelta(seconds=1)
#     oneDay = oneSec * 24 * 60 * 60
#     now = datetime.datetime.now()
#     now = now + oneSec
#     now = now.strftime("%Y/%m/%d %H:%M:%S")
#     print(now)
#
#     yvalue = round(random.random(),2)
#     # print(yvalue)
#     rowData['value'] = [now,yvalue]
#     rowData['name'] = now
#     # print(data['name'])
#     # print(data['value'])
#     data.append(rowData)
#     time.sleep(1)
#     return data
#
# for i in range (1,10):
#     randomData()
#
# for x in range (1,len(data)):
#     print(data[x])

# class getCPUInfo:
#     def getDataByIp():
#         # 打开数据库连接
#         db = pymysql.connect(host,user,passwd,dbname)
#         # 使用cursor()方法获取操作游标
#         cursor = db.cursor()
#         # SQL 插入语句
#         sql = """select concat('{"name":"',createtime,'","value":["',createtime,'",',cpuload,']}')
#                   from cpuinfo where createtime >= '1998-09-03 00:01:06';"""
#         try:
#             # 执行sql语句
#             cursor.execute(sql)
#             # 获取所有记录列表
#             results = cursor.fetchall()
#             # for row in results:
#             #     content = row[0]
#             #     # 打印结果
#             #     print ("content=%s" % (content))
#             # 提交到数据库执行
#             db.commit()
#             return results
#         except Exception as e:
#            # Rollback in case there is any error
#            #print 'str(e):\t\t', str(e)
#            print (str(e))
#            db.rollback()
#         # 关闭数据库连接
#         db.close()

# a=getCPUInfo
#
# datas = a.getDataByIp()
# newStr = ''
# for row in datas:
#     content = str(row[0],encoding='utf-8')
#     newStr = str(content) + ','
#     # print(str(row[0],encoding='utf-8'))
#     # print ("content=%s" % ((newStr)))
#     print(newStr)

class insertData:
    '新增服务器，一台服务器上只能定义一个类型(code)的服务'
    def __init__(self,hostName,createTime):
        self.hostName=hostName
        self.createTime=createTime


    def insertCpuInfo(self):
        cpuLoad=random.random()
        # 打开数据库连接
        db = pymysql.connect(host,user,passwd,dbname)
        db.set_charset('utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        #设置字符集解决latin字符集的报错问题
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        # SQL 插入语句
        sql = """INSERT INTO cpuinfo(hostname,
                                     createtime,
                                     cpuload)
                 VALUES ('%s',
                         '%s',
                         '%s')""" % \
                        (self.hostName,
                         self.createTime,
                         cpuLoad)
        print (sql)
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except Exception as e:
           # Rollback in case there is any error
           #print 'str(e):\t\t', str(e)
           print (str(e))
           db.rollback()
        # 关闭数据库连接
        db.close()

    def insertMemInfo(self):
        cpuLoad = random.random()
        # 打开数据库连接
        db = pymysql.connect(host,user,passwd,dbname)
        db.set_charset('utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        #设置字符集解决latin字符集的报错问题
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        # SQL 插入语句
        sql = """INSERT INTO meminfo(hostname,
                                     createtime,
                                     cpuload)
                 VALUES ('%s',
                         '%s',
                         '%s')""" % \
                        (self.hostName,
                         self.createTime,
                         cpuLoad)
        print (sql)
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except Exception as e:
           # Rollback in case there is any error
           #print 'str(e):\t\t', str(e)
           print (str(e))
           db.rollback()
        # 关闭数据库连接
        db.close()
# print(datetime.datetime.now()-5)

for i in range (1,1000):
    b=insertData('host1',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    b.insertCpuInfo()
    b.insertMemInfo()

    c=insertData('host2',datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    c.insertCpuInfo()
    c.insertMemInfo()
    time.sleep(5)