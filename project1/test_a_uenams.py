#coding:utf8
__time__ = '2018/5/9 13:53'
__author__ = 'SYJ'

# -*- coding: utf-8 -*-
#导入各种库
import requests,arrow,yaml,sys
import configparser,inspect
import json
import unittest
import pymysql
import xlrd
import re,datetime
import http.client
import logging,os,excel,ddt
from common.loginBBLC import BBLC
from common.loginuen import  uenpay
from common.log import Log
from common.orc import Uenoracle
# from common.getexcel import excel

@ddt.ddt
class Uenpayams(unittest.TestCase):
    '''用户提现接口'''
    pass
    global data
    # testdata = excel.ExcelUtil("d:\\test.xlsx","Sheet1")
    # data1 = testdata.dict_data()
    # data = []
    # for a in data1:
    #     print (a)
    #     if a['drawamount'] is not '':
    #         # print ("不为空")
    #         data.append(a['drawamount'])
    # print (data)

    def get_current_function_name(self):
        return inspect.stack()[1][3]




    @classmethod
    def setUpClass(cls):
        '''初始化数据'''
        global cf, pk_id, logger, fh, ch
        utc = arrow.now()
        # utc = utc.replace(days=-1)
        nowtime = utc.format('YYYY-MM-DD')
        cf = configparser.ConfigParser()
        cf.read("config.ini",encoding='utf-8')

        '''获得类名和当前函数名'''
        cls.classname=Uenpayams().__class__.__name__
        cls.currentfun=Uenpayams().get_current_function_name()

        '''读取yaml配置'''
        global sql
        cls.read=Uenoracle().read_config()
        sql=cls.read['sql']['sql1']
        # print (sql)

        '''读取用例文件的路径以及名称'''
        script_path = os.path.realpath(__file__)
        filename = os.path.split(script_path)[1]

        '''定义日志'''
        cls.log=Log(filename)
        cls.log.info('执行开始%s---------------------------------------'%format(Uenpayams().get_current_function_name()))

        '''登录系统保持session'''
        requests.packages.urllib3.disable_warnings()
        url=cls.read['ams']['url']
        s = requests.session()
        cls.login=uenpay(s)
        cls.login.login(url)


        '''查询数据库用户信息'''
        cls.Oracle=Uenoracle()





    @classmethod
    def tearDownClass(cls):
        '''关闭数据库'''
        # cls.conn.close()
        cls.log.info('执行结束%s---------------------------------------' % format(Uenpayams().get_current_function_name()))



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

    @unittest.skip
    # @ddt.data(*data)
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

    def test_3uenpay(self):
        '''用户管理系统'''
        # self.log.info('执行开始%s---------------------------------------' % format(Uenpayams().get_current_function_name()))
        # self.log.info('执行开始%s---------------------------------------' % format(Uenpay().get_current_function_name()))
        # self.log.info('请求数据:%s'%(data_test['data']))
        # body={'page':'1',
        #       'rows':'10',
        #       'shopName':'',
        #       'shopNo':'',
        #       'orgName':'',
        #       'orgCode':'',
        #       'freezeStatus':'',
        #       'channelId':'',
        #       'remark':''
        #       }
        body={}
        header=self.read['header']['header']
        url='https://test.uenpay.com/uenams/common/menu/admin'
        req=self.login.Uen(fangshi='POST',url=url,param=body,headers=header)#str要转成dict，req里才能用json
        print (req[0]['children'][0]['text'])
        # self.log.info(req[0]['children'][0]['text'])
        self.assertEqual('用户管理',req[0]['children'][0]['text'],'gg思密达')
        result=self.Oracle.orc_select(sql)    #调用数据库函数查询数据库数据进行断言
        print (result)



if __name__ == '__main__':
    # a=Uenpay()
    # print (a.get_current_function_name())

    unittest.main
