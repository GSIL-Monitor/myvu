# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow,os,ddt,random
import configparser
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging,excel
from common.loginBBLC import BBLC
from common.log import Log
from common.getexcel import excel
from common.sql import sql

path = "D:\jiekou-python3-master\\test_case\case.xlsx"
sheetname = 'Sheet1'
ex = excel(path, sheetname)
data_test = ex.makedata()
sql = sql()
a =sql.qianyueyonghu()
print(a)
# print (data_test)
@ddt.ddt
class Addhuoqi(unittest.TestCase):
    '''投资理财计划'''
    # global data
    # testdata = excel.ExcelUtil("d:\\test.xlsx","Sheet1")
    # data1 = testdata.dict_data()
    # data = []
    # # for x in range(len(data1)):
    # #     data.append((data1[x]['amount']))
    # # print (data)
    # for a in data1:
    #     # print(a)
    #     if a['choujiang'] is not '':
    #         # print ("不为空")
    #         data.append(a['choujiang'])
    # print(data)



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
        cls.log=Log()
        cls.log.info('执行开始---------------------------------------')


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
        # cur = cls.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # sql = "SELECT * FROM fiz_plan WHERE dt_datetime_filled IS null AND dt_create_time LIKE '%"+nowtime+"%' GROUP BY dt_datetime_approved DESC LIMIT 5;'"     #直接找最近的一条审核通过的理财计划
        # cur.execute(sql)
        # cls.result = cur.fetchone()



    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        cls.conn.close()
        cls.log.info('执行结束---------------------------------------')

    @ddt.data(*a)
    def test_api(self,a):
        '''接口'''
        s=requests.session()
        self.login=BBLC(s)
        self.login.login(a)
        number=round(random.uniform(1,500),2)
        print (number)
        # number=round(random.uniform(50,2000),2)
        # url='http://192.168.1.133/bblc-web-v20/demand/confirm'
        #申购
        # data={"data":{"id":"8c96d9f1-69d8-4c4f-a503-1f6fc85f7bcd","amount":number,"password":"111111"},"meta":{"clientType":"0","pageCode":"demandConfirm"}}
        #赎回
        data={"data":{"tranAmount":number,"payPassword":"111111","configPassword":""},"meta":{"clientType":"0","pageCode":"userDemandRdmpsn"}}
        url='http://192.168.1.133/bblc-web-v20/demand/redemSubmit'
        req=self.login.BBLCQQ(fangshi='POST',url=url,param=data)
        print (req)

    # @ddt.data(*data)
    # def test_1QT_chou(self,data):
    #     '''宝箱商城抽奖'''
    #     self.log.info('start------------------------------------')
    #     self.log.info('投资钥匙个数:%s'%(data))
    #     req1 = self.login.chou(data)
    #     if int(data)<0:
    #         self.log.info('返回:%s'%(req1)
    #         self.assertIn('参数异常',req1['message']['content'])
    #     elif int(data)==0:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('参数异常', req1['message']['content'])
    #     elif 0<int(data)<=10:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('钥匙不足',req1['message']['content'])
    #     elif int(data)>10:
    #         self.log.info('返回:%s' % (req1))
    #         self.assertIn('参数异常',req1['message']['content'])
    #     self.log.info(('end-------------------------------------'))



if __name__ == '__main__':
     unittest.main