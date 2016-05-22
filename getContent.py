# encoding: UTF-8
import re
import requests
import sys
import pymongo
reload(sys)
sys.setdefaultencoding( "utf-8" )
connection = pymongo.MongoClient()
tdb = connection.weibo
dbInsert = tdb.myweibo

def getContent(StrPage):
    cook = {"Cookie": ""}
    url = 'http://weibo.cn/xxxxxxxxxx/profile?page=' + StrPage		# 其中x为UID账号
    html = requests.get(url, cookies = cook)
    regexOrigin = re.compile(ur'<div class="c" id="M_(\w{9})"><div><span class="ctt">(.*?)</span>.*?cmtfrm" class="cc">评论\[(\d{1,2})\]</a>.*?class="ct">(\d{2}月\d{2}日|[\d-]{10}) ([\d:]{5,8})&nbsp;来自(.*?)</span>')
    regexPost = re.compile(ur'<div class="c" id="M_(\w{9})"><div><span class="cmt">转发了&nbsp;<a href="(.*?)</a>.*?class="ctt">(.*?)</span>&nbsp;.*?class="cmt">转发理由:</span>(.*?)&nbsp;&nbsp;<a href="http://weibo.cn/attitude.*?class="cc">评论\[(\d{1,2})\]</a>.*?class="ct">(\d\d月\d\d日|[\d-]{10}) ([\d:]{5,8})&nbsp;来自(.*?)</span></div></div>')
    originalKey = ['code', 'post', 'numComment', 'date', 'time', 'wherefrom']
    repostKey = ['code', 'originalAuthor', 'originalContent', 'repostContent', 'numComment', 'date', 'time', 'wherefrom']
    
    for i in range(len(originalContent)):
        text = ''
        originalList = []
        for j in range(6):
            originalList.append(originalContent[i][j].encode("utf8"))
            print originalContent[i][j].encode("utf8")
            text = text + str(originalContent[i][j]) + '\n'
        originalDict = dict(zip(originalKey, originalList))
        numComment = int(originalContent[i][2])
        if numComment != 0:
            print 'have comment!'
            originalTextCode = originalTextCode + str(originalContent[i][0]) + '/'
            originalDict['comment']=getComment.getComment(str(content[i][0]))
        dbInsert.insert(originalDict)         
        textContent = open('textWeibo.txt','a')
        textContent.write(text)
        textContent.write("\n++++++++++++++++++++++++++++++++++\n")
        textContent.close()
        print '++++++++++++++++++++++++++++++++++'
    print 'aa'
    print originalTextCode
    f = open('weiboContentCode.txt','a')
    f.write(originalTextCode)
    f.close()

getContent('1')
