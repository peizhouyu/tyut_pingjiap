# coding: gbk
import urllib.request
import string
import re
import json
import sys,os
import config
import http.cookiejar,time,urllib.parse,urllib.error
import random
import commonFunction

# postdata = urllib.parse.urlencode({
#         '0000000136':'25_0.95',
#         '0000000137':'25_0.95',
#         '0000000138':'30_0.95',
#         '0000000139':'20_0.95',
#         'zgpj':"��ʦ����������������һλ�ѵõĺ���ʦ��",
#
#     }).encode(encoding='gbk',errors='strict')
#
# print(postdata)

# a = u"����"
# a_gb2312 = a.encode('gbk')
# print (a_gb2312.decode('gb2312'))

string = u"��ʦ����������������һλ�ѵõĺ���ʦ��"
stringGBK = string.encode('gbk')
postdata = urllib.parse.urlencode({

    '0000000136': '25_0.95',
    '0000000137': '25_0.95',
    '0000000138': '30_0.95',
    '0000000139': '20_0.95',
    'zgpj': stringGBK,

}).encode('GBK')
print(postdata)