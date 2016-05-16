# encoding: UTF-8
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def getContent(StrPage):
    cook = {"Cookie": ""}
    url = 'http://weibo.cn/xxxxxxxxxx/profile?page=' + StrPage		# 其中x为UID账号
    html = requests.get(url, cookies = cook)
    reOrigin = re.compile(ur'<div class="c" id="M_(\w+)"><div><span class="ctt">(.*?)</span>.*?cmtfrm" class="cc">评论\[(\d)\]</a>.*?class="ct">(\d{2}月\d{2}日) ([\d:]{4,10})&nbsp;来自(.*?)</span>')
    content = re.findall(reOrigin,html.text)
    textToken = ''
    for i in range(len(content)):
        text = ''
        for j in range(6):
            print content[i][j].encode("utf8")
            text = text + str(content[i][j]) + '\n'
        numComment = int(content[i][2])
        if numComment != 0:
            print 'had comment!'
            textToken = textToken + str(content[i][0]) + '/'
        textContent = open('textWeibo.txt','a')
        textContent.write(text)
        textContent.write("\n++++++++++++++++++++++++++++++++++\n")
        textContent.close()
        print '++++++++++++++++++++++++++++++++++'
    print textToken     # 有评论内容的微博
    f = open('weiboContentToken.txt','a')
    f.write(textToken)
    f.close()

getContent('1')
