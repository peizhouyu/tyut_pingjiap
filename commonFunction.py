import config
import http.cookiejar,time,urllib.parse,urllib.error
import random

#读取本地cookie文件 初始化请求
def loadCookie():
    # 创建MozillaCookieJar实例对象
    cookie = http.cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    return cookie

