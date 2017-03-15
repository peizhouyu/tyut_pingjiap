
JWCURL = "http://219.226.101.61/jiawu3.html"
#主url
URL = "http://202.207.247.49/"
URL2 = "http://202.207.247.44:8064/"
URL3 = "http://202.207.247.44:8065/"
URL4 = "http://202.207.247.44:8069/"
#login
URL_LOGIN = "loginAction.do"
#学籍信息
URL_XJXX = "xjInfoAction.do?oper=xjxx"
#学分绩点
URL_XFDJ = "gradeLnAllAction.do?oper=xfjd"
#实践成绩
URL_ZJSJ = "xszzsjcjbAction.do?oper=viewByStudent"
#本学期课表
URL_KB = "syglSyxkAction.do?&oper=xsxkKcbAll"
#本学期成绩
URL_BXQCJ = "bxqcjcxAction.do"
#验证码
URL_YZM = "validateCodeAction.do"
#照片
URL_ZP = "xjInfoAction.do?oper=img"
#方案成绩
URL_FA = "gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=1734"
#全部及格成绩
URL_QB = "gradeLnAllAction.do?type=ln&oper=qbinfo"
#不及格成绩
URL_BJG = "gradeLnAllAction.do?type=ln&oper=bjg"
#通知公告
URL_TZGG = "detail.asp?bigid=7"
#jwc网站
URL_JWC = "http:#jwc.tyut.edu.cn/"
#评教列表
URL_JXPG_LIST = "jxpgXsAction.do?oper=listWj"
#具体评估
URL_JXPG = "jxpgXsAction.do?oper=wjpg"
#评估页面
URL_PG = "jxpgXsAction.do"
#返回数据错误
NET_FAIL = "FAIL"
#session失效
SESSION_FAIL = "SESSION_FAIL"

#handler   返回数据成功
DATA_SUCCESS = 0x01
#handler 返回数据失败
DATA_FAIL = 0x02
#handler 返回验证码失败
YZM_FAIL = 0x03
#handler session 失效
SESSION = 0x04
#handler 验证码成功
YZM_SUCCESS = 0x05
#评估成功
PG_SUCCESS = 0x06
