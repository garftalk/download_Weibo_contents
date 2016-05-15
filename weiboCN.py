# encoding: UTF-8
import re
import sys
import time
import requests
reload(sys)
sys.setdefaultencoding( "utf-8" )


def getContent(StrPage):
    cook = {"Cookie": "h5_deviceID=3740261c346dfd5071c75a995a24fae1; _T_WM=2d10da6f3d1689747e99cd306c9c4c06; _WEIBO_UID=2246893364; SUB=_2A256Mv4YDeTxGeRM71QZ-S3PzTiIHXVZ3IJQrDV6PUJbstBeLVjXkW1LHes16n5EUJX29E8sHO-M6BtUQDLWGw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh928kaLnVvShrZMdzSdWIG5JpX5o2p5NHD95QEeoBc1h.0e0qX; SUHB=0pHgt6NnsWbBn4; SSOLoginState=1463193160; gsid_CTandWM=4uGCCpOz5cYj4YPYpNEZ69qwd5S"}

    url = 'http://weibo.cn/2246893364/profile?page=3&retcode=6102'
    # url = 'http://weibo.cn/2246893364/profile?page=' + StrPage
    # html = requests.get(url).content
    # print html
    html = requests.get(url, cookies = cook)
    print 'aa'
    reGetContent = re.compile(ur'<div class="c" id="M_(\w+)"><div><span class="ctt">(.*?)</span>.*?cmtfrm" class="cc">评论\[(\d)\]</a>.*?class="ct">(\d{2}月\d{2}日) ([\d:]{4,10})&nbsp;来自(.*?)</span>')
    content = re.findall(reGetContent,html.text)
    textToken = ''
    print content
    for i in range(len(content)):
        yuanchuang = ''
        for j in range(6):
            print content[i][j].encode("utf8")
            yuanchuang = yuanchuang + str(content[i][j])
        numComment = int(content[i][2])
        if numComment != 0:
            print 'have comment!'
            textToken = textToken + str(content[i][0]) + '\r\n'
        yuanchuang += '--------------------------------------'
        yuanchuangContent = open('yuanchuangWeibo.txt','a')
        yuanchuangContent.write(yuanchuang)
        yuanchuangContent.close()
        print '------------------------------------'
    print 'aa'
    print textToken
    f = open('weiboContentToken.txt','a')
    f.write(textToken)
    f.close()

if __name__ == "__main__":
    for Page in range(5,6):
        StrPage = str(Page)
        getContent(StrPage)
        print 'hhh'