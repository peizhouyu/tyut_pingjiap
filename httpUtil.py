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
    #����cookie
    cookie = commonFunction.loadCookie()
    # ���������request
    req = urllib.request.Request(url,postdata, header)
    # ����urllib2��build_opener��������һ��opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    # print (response.read().decode('GBK'))
    getCourseList()

#��ȡ�����۵Ŀγ��б�
def getCourseList():
    url = config.URL + config.URL_JXPG_LIST
    # ����cookie
    cookie = commonFunction.loadCookie()
    # ���������request
    req = urllib.request.Request(url)
    # ����urllib2��build_opener��������һ��opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)

    html = response.read().decode('GBK')
    #����ƥ���ȡÿ�ſξ������Ϣ������������õ���post������
    html_select = re.findall('<img name="(\d+)#@(.+)#@(.+)#@(.+)#@(.+)#@(.+)"', html)
    print(len(html_select))
    for n in range(len(html_select)):
        wjbm = html_select[n][0]
        bpr = html_select[n][1]
        html_select[n][3]
        pgnr = html_select[n][5]

        bprm = html_select[n][2]
        pgnrm = html_select[n][4]

        # print(html_select[n][0])
        # print(html_select[n][1])
        # print(html_select[n][2])
        #print(html_select[n][4])
        # print(html_select[n][4])
        # print(html_select[n][5])

        print('------------------')



        beforeSendInfo(wjbm,bpr,pgnr,bprm,pgnrm)
        sendInfo(wjbm,bpr,pgnr)
        #time.sleep(1)






#����ǰ����
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
    print("����ǰ����")
    print("wjbm---"+wjbm)
    print("bpr---" + bpr)
    print("pgnr---" + pgnr)
    print("oper---" + "wjShow")
    print("wjmc---" + '2017-2018ѧ���＾ѧ����������')
    print("bprm---" + bprm)
    print("pgnrm---" + pgnrm)
    print("wjbm---" + wjbm)

    postdata = urllib.parse.urlencode({
        'wjbm': wjbm,
        'bpr': bpr,
        'pgnr': pgnr,
        'oper': 'wjShow',
        'wjmc': '2017-2018ѧ���＾ѧ����������',
        'bprm': bprm,
        'pgnrm':pgnrm,
        'pageSize': '20',
        'page': '1',
        'currentPage': '1',
        'pageNo': '',

    }).encode('GBK')
    # ����cookie
    cookie = commonFunction.loadCookie()
    # ���������request
    req = urllib.request.Request(url, postdata, header)
    # ����urllib2��build_opener��������һ��opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)

    #print(response.read().decode('GBK'))
    print(response.read())

    return response.read()




#������������
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
    string = u"��ʦ����������������һλ�ѵõĺ���ʦ��"
    stringGBK = string.encode('gbk')
    postdata = urllib.parse.urlencode({
        'wjbm': wjbm,
        'bpr': bpr,
        'pgnr': pgnr,
        '0000000045':'10_1',
        'zgpj':stringGBK,

    }).encode('GBK')
    # ����cookie
    cookie = commonFunction.loadCookie()
    # ���������request
    req = urllib.request.Request(url, postdata, header)
    # ����urllib2��build_opener��������һ��opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    # print('-------')
    # print(postdata)
    print(response.read().decode('GBK'))


#�鿴������Ϣ
def showInfo():
    url = config.URL + config.URL_XJXX
    # ����cookie
    cookie = commonFunction.loadCookie()
    # ���������request
    req = urllib.request.Request(url)
    # ����urllib2��build_opener��������һ��opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print (response.read().decode('GBK'))



#��ȡ��֤��
def getCode():
    rand = random.uniform(0, 1)
    # ����һ��MozillaCookieJar����ʵ��������cookie��֮��д���ļ�
    cookie = http.cookiejar.MozillaCookieJar(filename)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    url = config.URL + config.URL_YZM + "?random=" + str(rand)
    result = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    print(url)
    return result.read()

if __name__ == "__main__":
    getCode()