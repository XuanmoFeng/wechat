# -*- coding: utf-8 -*-
# filename: handle.py
from  string  import maketrans
import hashlib
import web
import reply
import Xatu
import www
import receive
class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "weixin" #请按照公众平台官网\基本配置中信息填    
            list = [token, timestamp, nonce]
            list.sort()                        
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument
    def POST(self):
        try:
            webData=web.data()
            #print "Handle Post webData is ",webData
            recMsg =receive.parse_xml(webData)
            if isinstance(recMsg,receive.Msg) and recMsg.MsgType =='text':
                toUser=recMsg.FromUserName#client
                fromUser=recMsg.ToUserName#server
                UserText=recMsg.Content
                if UserText=="成绩":
                    content=www.Grade(toUser)
                elif UserText.count('&')==1:##绑定
                    ind ="&"
                    optd ="@"
                    trantab = maketrans(ind,optd)  
                    UserText=UserText.translate(trantab)
                    content=www.Bind(toUser,UserText)
                replyMsg=reply.TextMsg(toUser,fromUser,content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception,Argument:
            return Argument
