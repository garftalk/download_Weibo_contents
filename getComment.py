# encoding: UTF-8
import re
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getComment(contentToken):   # 参数为每条微博对应的唯一的一个字符串，使用weibo.cn打开一条微博的评论就能看到
    cook = {"Cookie": ""}       # cookie为自己账号的cookie值
    url = 'http://weibo.cn/comment/' + contentToken
    html = requests.get(url, cookies=cook)
    allComment = []

    reGetComment = re.compile(ur'<div class="c" id="C.*?<a href=(.*?)</a>.*?<span class="ctt">(.*?)</span>.*?<span class="ct">(\d\d月\d\d日|[\d-]{10}) ([\d:]{4,10})&nbsp;来自(.*?)</span></div>')
    reGetPage = re.compile(ur'1/(\d+)页')
    content = re.findall(reGetComment, html.text)
    commentPage = re.findall(reGetPage, html.text)
    NumPage = int(commentPage[0])
    print commentPage
    print NumPage
    filename = '微博' + contentToken + '的评论'
    for i in range(len(content)):
        oneComment = []
        for j in range(5):
            print content[i][j]
            oneComment.append(content[i][j])
            f = open(filename, 'a')
            f.write(str(content[i][j]))
            f.write('\n')
        f.write('--------------------------------\n')
        print '-------------------------------'
        allComment.append(oneComment)
    f.close()
    if NumPage >= 2:
        for i in range(2, NumPage+1):
            nextPageUrl = 'http://weibo.cn/comment/' + contentToken + '?page=' + str(i)
            html = requests.get(nextPageUrl, cookies=cook)
            content = re.findall(reGetComment, html.text)
            for i in range(len(content)):
                oneComment = []
                for j in range(5):
                    print content[i][j]
                    oneComment.append(content[i][j])
                    f = open(filename, 'a')
                    f.write(str(content[i][j]))
                    f.write('\n')
                f.write('--------------------------------\n')
                print '-------------------------------'
                allComment.append(oneComment)
        f.close()
    print allComment
    return allComment
    
getComment('') # 参数为每条微博唯一的字符串，点击评论之后能在地址中看到
