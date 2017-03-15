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
#         'zgpj':"老师讲课认真生动，是一位难得的好老师！",
#
#     }).encode(encoding='gbk',errors='strict')
#
# print(postdata)

# a = u"中文"
# a_gb2312 = a.encode('gbk')
# print (a_gb2312.decode('gb2312'))

string = u"老师讲课认真生动，是一位难得的好老师！"
stringGBK = string.encode('gbk')
postdata = urllib.parse.urlencode({

    '0000000136': '25_0.95',
    '0000000137': '25_0.95',
    '0000000138': '30_0.95',
    '0000000139': '20_0.95',
    'zgpj': stringGBK,

}).encode('GBK')
print(postdata)