#!/usr/bin/env python
# coding=utf-8
import DataBase
import Xatu
import string
def Grade(weid):
    if DataBase.Select(weid)==" ":
        return "请绑定格式如：\n14050205101&xasdascas"
    else:
        print "Grade\n"
        str=DataBase.Select(weid)
        user=str.partition('@')
        username=user[0]
        password=user[2]
        result=Xatu.Str(username,password)
        if result == "FALSE":
            return "查询失败请重新绑定\n"
        else:
            return result

def Bind(weid,str):
    user=str.partition('@')
    username=user[0]
    password=user[2]
    if DataBase.InsertData(weid,username,password)=="1":
        return "绑定成功\n"
    else:
        return "请检查账号和密码是否错误\n"
