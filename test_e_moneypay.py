# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow
import configparser
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging,os,ddt,xlrd
import excel,threading

@ddt.ddt
class AddChong(unittest.TestCase):
    '''用户充值接口'''
    global data
    testdata = excel.ExcelUtil("d:\\test.xlsx","Sheet1")
    data1 = testdata.dict_data()
    data = []
    # for x in range(len(data1)):
    #     data.append((data1[x]['amount']))
    # print (data)
    for a in data1:
        # print(a)
        if a['amount'] is not '':
            # print ("不为空")
            data.append(a['amount'])
    print(data)



    @classmethod
    def setUpClass(cls):
        '''初始化数据'''
        global cf, pk_id, logger, fh, ch
        utc = arrow.now()
        # utc = utc.replace(days=-1)
        nowtime = utc.format('YYYY-MM-DD')
        cf = configparser.ConfigParser()
        cf.read("config.ini",encoding='utf-8')
        # s = cf.sections()
        # print("section:", s)
        cls.bbl_login = cf.get("url","bbl_login")
        cls.console_login = cf.get("url","console_login")

        '''定义日志'''
        logger = logging.getLogger('BBLC')
        # defined log level
        logger.setLevel(logging.DEBUG)

        # defined handler
        proDir = os.path.realpath("D:\pythonstudy\python3\\log")
        fh = logging.FileHandler(os.path.join(proDir, "output.log"))
        ch = logging.StreamHandler()
        # defined formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # fh.setLevel(logging.DEBUG)
        # ch.setLevel(logging.DEBUG)
        # add handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info('开始执行AddChong---------------------------------------')

        '''查询数据库用户信息'''
        db_host = cf.get("mysql","host")
        db_user = cf.get("mysql", "user")
        db_password = cf.get("mysql", "password")
        db_database = cf.get("mysql", "database")
        db_charset = cf.get("mysql","charset")
        db_port = cf.get("mysql","port")
        # print ("db_host:",db_host)
        # print ("db_user:",db_user)
        # print ("db_password:",db_password)
        # print ("db_database:",db_database)
        # print ("db_charset:",db_charset)
        # print ("db_port:",db_port)
        # cls.conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_database,charset=db_charset)
        # cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # sql = "SELECT * FROM fiz_plan WHERE dt_datetime_filled IS null AND dt_create_time LIKE '%"+nowtime+"%' GROUP BY dt_datetime_approved DESC LIMIT 5;'"     #直接找最近的一条审核通过的理财计划
        # cur.execute(sql)
        # cls.result = cur.fetchone()
        # pk_id = cls.result['pk_id']



    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        # cls.conn.close()
        logger.info('执行结束AddChong---------------------------------------')
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    # @unittest.skip
    def test_1QT_login(self):
        '''前台用户登录'''
        global request
        request = requests.session()
        self.i=cf.get("keren","yonghu")
        # print (self.i)
        account = ["17612129080", "18516013908", "18621137962", "13761917640", "13816997392", "18221382710","18603826221","13761917640"]
        password = ["111111", "111111", "111111", "a111111", "111111", "111111", "111111","a111111"]
        url = 'http://192.168.1.133/bblc-web-v20/user/authenticate'
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
            "Origin": "http://192.168.1.133",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8"}
        print ("投资人电话号码:%s"%(account[int(self.i)]))       #打印投资人的电话号码
        body = {"data":
                    {"account": account[int(self.i)], "password": password[int(self.i)]},
                "meta":
                    {"clientType": "0", "pageCode": "userSignIn"}
                }
        # body = {"account": account[int(self.i)],        #转整数
        #         "password": password[int(self.i)]}
        req=request.post(url,headers=header,json=body)
        R = json.loads(req.text,encoding='utf-8')
        # print (R)
        # logging.info('登录成功！')
        # self.assertEqual(R['type'],'SUCCESS',msg='登录失败！')
        # logger.info('登录成功')
        logger.info('test_1QT_login用例通过！')

    # @unittest.skip('TZ用例调试停用')
    def test_2token1(self):
        global token1
        url = "http://192.168.1.133/bbl-web/user/fuyouPay"
        # headers = {
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #     "Accept-Language": " zh-CN,zh;q=0.8",
        #     "Accept-Encoding": "gzip, deflate",
        #     "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
        #     "Cookie": cookie1}
        req = request.get(url)
        res = req.text
        # print (res)
        token = re.findall(r"name=\"token1\"\s+value=\"(.*?)\"", res)
        logger.info(token[0])
        token1 = token[0]
        if token1:
            logger.info('test_2token1用例通过！')
        return token1

    # @unittest.skip('TZ用例调试停用')
    @ddt.data(*data)
    def test_2chong(self,data):
        '''用户充值'''
        self.amount = cf.get('chongzhi','amount')
        self.payPassword = cf.get('chongzhi','payPassword')
        self.num = cf.get('chongzhi','num')
        url = 'http://192.168.1.133/bblc-web-v20/recharge/submit'
        # url1 = "http://192.168.1.133/bblc-web-v20/recharge/submit"
        # req1 = request.get(url1)
        # res1 = req1.text
        # token = re.findall(r"name=\"token1\"\s+value=\"(.*?)\"", res1)
        # token1 = token[0]
        num = -50
        while num <= int(self.num):
            #查询token
            # req1 = request.get(url1)
            # res1 = req1.text
            # token = re.findall(r"name=\"token1\"\s+value=\"(.*?)\"", res1)
            # token1 = token[0]
            #进行充值
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
                "Origin": "http://192.168.1.133",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/json;charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "http://192.168.1.133/bblc-web-v20/mall/list.html",
                "Upgrade-Insecure-Requests": "1"}
            body = {"data":{"tranAmount":data,"payPassword":"111111","configPassword":""},"meta":{"clientType":"0","pageCode":"userQuickRecharge"}}
            print("充值金额为:%s" % (data))
            req = request.post(url,headers=headers,json=body)
            # res = json.loads(req.text,encoding='utf-8')
            res = req.json()
            logger.info(res)
            self.assertEqual(res['message']['code'] ,'0')
            num +=1
        logger.info('test_2chong用例通过！')
        # print (res)

if __name__ == '__main__':
    unittest.main
    # threads = []
    # t1 = threading.Thread(target=AddChong.test_1QT_login(AddChong))
    # threads.append(t1)
    # t2 = threading.Thread(target=AddChong.test_1QT_login(AddChong))
    # threads.append(t2)
    # for t in threads:
    #     # t.setDaemon(True)
    #     t.start()
