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
import logging,os,excel,ddt
from common.loginBBLC import BBLC
from common.log import Log
# from common.getexcel import excel

@ddt.ddt
class Adddrawout(unittest.TestCase):
    '''用户提现接口'''
    global data
    testdata = excel.ExcelUtil("d:\\test.xlsx","Sheet1")
    data1 = testdata.dict_data()
    data = []
    for a in data1:
        print (a)
        if a['drawamount'] is not '':
            # print ("不为空")
            data.append(a['drawamount'])
    print (data)



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
        logger.info('开始执行Adddrawout---------------------------------------')
        s=requests.session()
        cls.login=BBLC(s)
        cls.login.login('13761917640')


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
        logger.info('执行结束Adddrawout---------------------------------------')
        logger.removeHandler(fh)
        logger.removeHandler(ch)


    @unittest.skip
    def test_1QT_login(self):
        '''前台用户登录'''
        global request
        request = requests.session()
        self.i=cf.get("keren","yonghu")
        # print (self.i)
        account = ["17612129080", "18516013908", "18621137962", "13761917640", "13816997392", "18221382710"]
        password = ["111111", "111111", "111111", "a111111", "111111", "111111"]
        url = 'http://192.168.1.133/bbl-web/authenticate'
        # print (account[int(self.i)])        #打印投资人的电话号码
        body = {"account": account[int(self.i)],        #转整数
                "password": password[int(self.i)]}
        req=request.post(url,body)
        R = json.loads(req.text,encoding='utf-8')
        print (R)
        # logging.info('登录成功！')
        self.assertEqual(R['type'],'SUCCESS',msg='登录失败！')
        # logger.info('登录成功')
        logger.info('test_1QT_login用例通过！')

    # @unittest.skip
    @ddt.data(*data)
    def test_2tixian(self,data):
        '''用户提现'''
        self.drawoutamount = cf.get('tixian','amount')
        self.payPassword = cf.get('tixian','payPassword')
        self.num = cf.get('tixian','num')
        url = 'http://192.168.1.133/bblc-web-v20/withDraw/submit'
        url1 = "http://192.168.1.133/bbl-web/user/fuyouPay"
        # req1 = request.get(url1)
        # res1 = req1.text
        # token = re.findall(r"name=\"token1\"\s+value=\"(.*?)\"", res1)
        # print (token)
        # token1 = token[0]
        #查询token
        #进行充值
        print ("提现金额;%s"%(data))
        # body = {"token1": token1,
        #         "amount": data,
        #         "payPassword": self.payPassword}
        body={"data":{"tranAmount":data,"payPassword":"111111","configPassword":"","token1":"90473621-9771-4383-9bfd-026c52c84832"},"meta":{"clientType":"0","pageCode":"userWithdraw"}}
        res=self.login.BBLCQQ('POST',url,body)
        # print (res)
        # req = request.post(url,json=body)
        # res = json.loads(req.text,encoding='utf-8')
        # res=req.json()
        # logger.info(res)
        print (res)
        self.assertEqual(res['message']['content'],'提现申请成功')
        logger.info('test_2chong用例通过！')



if __name__ == '__main__':
    unittest.main
