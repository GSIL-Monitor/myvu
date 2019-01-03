# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow,os
import configparser
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging


class AddTZ(unittest.TestCase):
    '''投资理财计划'''



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
        logger.info('开始执行AddTZ---------------------------------------')

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
        cls.conn = pymysql.connect(host=db_host, user=db_user, passwd=db_password, db=db_database,charset=db_charset)
        # self.conn = pymysql.connect(host='192.168.1.132', user='bbq', passwd='bbq123456',port=3306, db='bbq_financz_test',charset='utf8')
        # self.conn = pymysql.connect(host='192.168.1.132' ,user='bbq', passwd='bbq123456',port=3306,db='bbq_financz_test',charset='utf8')
        cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from fiz_plan where vc_name='理财计划-1102' order by dt_create_time DESC"     #直接找最近的一条审核通过的理财计划
        cur.execute(sql)
        cls.result = cur.fetchone()
        # print (self.result)
        # for data in self.result:
        #     print (data[0],data[1])
        # print ("pk_id:%s"%(self.result['pk_id']))
        # logger.info("pk_id:%s"%(self.result['pk_id']))
        pk_id = cls.result['pk_id']
        # print (pk_id)
        # print ("pk_id:%s"%(cur.description[1][0]))
        # print ("pk_id:%s,nb_balance:%s,vc_name:%s,vc_account:%s,dc_type:%s"%(self.result['pk_id'],self.result['nb_balance'],self.result['vc_name'],self.result['vc_account'],self.result['dc_type']))


    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        logger.info('执行结束AddTZ---------------------------------------')
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def test_1QT_login(self):
        '''前台用户登录'''
        global request
        request = requests.session()
        self.i=cf.get("keren","yonghu")
        # print (self.i)
        account = ["17612129080", "18516013908", "18621137962", "13761917640", "13816997392", "18221382710","18603826221","13761917640"]
        password = ["111111", "111111", "111111", "a111111", "111111", "111111", "111111","a111111"]
        url = 'http://192.168.1.133/bbl-web/authenticate'
        print (account[int(self.i)])        #打印投资人的电话号码
        body = {"account": account[int(self.i)],        #转整数
                "password": password[int(self.i)]}
        req=request.post(url,body)
        R = json.loads(req.text,encoding='utf-8')
        print (R)
        # logging.info('登录成功！')
        self.assertEqual(R['type'],'SUCCESS',msg='登录失败！')
        # logger.info('登录成功')
        logger.info('test_1QT_login用例通过！')
        # else:
        #     logging.info('登录失败！')
        #     print (str(AssertionError))
        #     # print ('登录成功')
        # else:
            # logging.info('登录失败！')

    # @unittest.skip('TZ用例调试停用')
    def test_2TZ(self):
        '''投资理财计划'''
        lcamount=cf.get("LCJH","amount")
        amount=cf.get("amount","amount")
        # n=float(int(lcamount)/10000)
        # logger.info(n)
        # logger.info(lcamount)
        # print (lcamount)
        # n1=1
        # for n1 in range(int(n)):
        url = 'http://192.168.1.133/bbl-web/plan/invest'
        body = {"id": pk_id,
                "amount": lcamount,
                "redPacketId": ""}
        req=request.post(url,body)
        # r=json.loads(req.text,encoding='utf-8')
        r = req.text
        # response = opener.open(req)
        # print (r)
        r1 = re.findall(r"class=\"txt\">(.*?)<", r)
        # print r1[0]
        if r1:
            # print (r)
            logger.info(pk_id)
            print("投资结果：“%s”" % (r1[0]))
            self.assertEqual(r1[0],'购买成功！',msg='购买失败！')
            logger.info('test_2TZ用例不通过！')
        else:
            r2 = re.findall(r"\"top_tips\"\>(.*?)<", r)
            print(r2[0])
            # print "提示为空"

if __name__ == '__main__':
     unittest.main