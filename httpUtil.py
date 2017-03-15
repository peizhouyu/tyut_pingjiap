# -*- coding: gbk -*-
import urllib.request
import string
import re
import json
import sys,os
import config
import http.cookiejar,time,urllib.parse,urllib.error
import random
import commonFunction

filename = 'cookie.txt'

def doLogin(number,password,checkimg):
    url = config.URL + config.URL_LOGIN
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        # 'Host': '',
    }
    postdata = urllib.parse.urlencode({
        'zjh': number,
        'mm': password,
        'v_yzm':checkimg,

    }).encode('GBK')
    #载入cookie
    cookie = commonFunction.loadCookie()
    # 创建请求的request
    req = urllib.request.Request(url,postdata, header)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    # print (response.read().decode('GBK'))
    getCourseList()

#获取需评价的课程列表
def getCourseList():
    url = config.URL + config.URL_JXPG_LIST
    # 载入cookie
    cookie = commonFunction.loadCookie()
    # 创建请求的request
    req = urllib.request.Request(url)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)

    html = response.read().decode('GBK')
    #正则匹配获取每门课具体的信息用来构造后面用到的post请求体
    html_select = re.findall('<img name="(\d+)#@(.+?)#@(.+?)#@.+?#@(.+?)#@(.+?)"', html)
    print(len(html_select))
    for n in range(len(html_select)):
        wjbm = html_select[n][0]
        bpr = html_select[n][1]
        html_select[n][3]
        pgnr = html_select[n][4]

        bprm = html_select[n][2]
        pgnrm = html_select[n][3]

        # print(html_select[n][0])
        # print(html_select[n][1])
        # print(html_select[n][2])
        # print(html_select[n][3])
        # print(html_select[n][4])
        #
        # print('------------------')



        beforeSendInfo(wjbm,bpr,pgnr,bprm,pgnrm)
        sendInfo(wjbm,bpr,pgnr)
        time.sleep(1)


def get_paper_form_postdata(wjbm,bpr,pgnr,L = []):
    if len(L) == 0:
        postDict = {
            'wjbm': wjbm,
            'bpr': bpr,
            'pgnr': pgnr,
            'oper': 'wjShow',
            # 'wjmc':'2014-2015-2%CC%E5%D3%FD%BF%CE',      #fuck !     what the hell is that!
            # 'bprm':'%CE%E2%B1%F6',                                                                     #fuck !     what the hell is that!
            # 'pgnrm':'%CC%E5%D3%FD%A3%A8%B6%FE%A3%A9',                  #fuck !     what the hell is that!
            'pageSize': '20',
            'page': '1',
            'currentPage': '1',
            'pageNo': ''
        }
    else:
        postDict = {
            'wjbm': wjbm,
            'bpr': bpr,
            'pgnr': pgnr,
            #  'zgpj':
        }
        for x in L:
            postDict[x] = '10_1'  # 默认全都是最好想修改去urp看每个评级的值

    postData = urllib.parse.urlencode(postDict).encode()
    return postData





#请求前操作
def beforeSendInfo(wjbm,bpr,pgnr,bprm,pgnrm):
    url = config.URL + config.URL_PG
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        # 'Host': '',
    }
    postdata = urllib.parse.urlencode({
        'wjbm': wjbm,
        'bpr': bpr,
        'pgnr': pgnr,
        'oper': 'wjShow',
        'wjmc': '2016-2017学年第一学期学生期末评教',
        'bprm': bprm,
        'pgnrm':pgnrm,
        'pageSize': '20',
        'page': '1',
        'currentPage': '1',
        'pageNo': '',

    }).encode('GBK')
    # 载入cookie
    cookie = commonFunction.loadCookie()
    # 创建请求的request
    req = urllib.request.Request(url, postdata, header)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)

    #print(response.read().decode('GBK'))
    #print(response.read())
    return response.read()




#发送评价请求
def sendInfo(wjbm,bpr,pgnr):
    url = config.URL + config.URL_JXPG
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept-Encoding': 'gzip, deflate',
        # 'Host': '',
    }
    string = u"老师讲课认真生动，是一位难得的好老师！"
    stringGBK = string.encode('gbk')
    postdata = urllib.parse.urlencode({
        'wjbm': wjbm,
        'bpr': bpr,
        'pgnr': pgnr,
        '0000000136':'25_0.95',
        '0000000137':'25_0.95',
        '0000000138':'30_0.95',
        '0000000139':'20_0.95',
        'zgpj':stringGBK,

    }).encode('GBK')
    # 载入cookie
    cookie = commonFunction.loadCookie()
    # 创建请求的request
    req = urllib.request.Request(url, postdata, header)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    # print('-------')
    # print(postdata)
    print(response.read().decode('GBK'))


#查看个人信息
def showInfo():
    url = config.URL + config.URL_XJXX
    # 载入cookie
    cookie = commonFunction.loadCookie()
    # 创建请求的request
    req = urllib.request.Request(url)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print (response.read().decode('GBK'))



#获取验证码
def getCode():
    rand = random.uniform(0, 1)
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = http.cookiejar.MozillaCookieJar(filename)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    url = config.URL + config.URL_YZM + "?random=" + str(rand)
    result = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    print(url)
    return result.read()

if __name__ == "__main__":
    getCode()