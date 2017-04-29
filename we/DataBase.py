#!/usr/bin/env python
# coding=utf-8

import MySQLdb

def CreateData():
    db=MySQLdb.connect("localhost","root","123456","xatu")
    cursor=db.cursor()
    sql = """CREATE TABLE EMPLOYEE (
            WEID  CHAR(100) NOT NULL,
            EUID  CHAR(20),
            EUPASS CHAR(20)  
           ) """
    cursor.execute(sql)
    db.close()
def InsertData(Weid,Euid,Eupass):
    db=MySQLdb.connect("localhost","root","123456","xatu") 
    cursor=db.cursor()
    sql="INSERT INTO EMPLOYEE(WEID,EUID,EUPASS) VALUES ('%s', '%s','%s')"%(Weid, Euid,Eupass)
    str="2"
    try:
        cursor.execute(sql)
        db.commit()
        str="1"
    except:
        db.rollback()
    db.close()
    return str

def Select(weid):
    db=MySQLdb.connect("localhost","root","123456","xatu") 
    cursor=db.cursor()
    sql ="SELECT * FROM EMPLOYEE WHERE WEID='%s'"%(weid)
    print sql
    try:# 执行SQL语句
        cursor.execute(sql)# 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            weid=row[0]
            username=row[1]
            password=row[2]
            str =username+"@"+password
    except:
        str=" "
        # 关闭数据库连接
    db.close()
    return str

