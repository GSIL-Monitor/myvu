#coding:utf8
__time__ = '2018/5/24 13:34'
__author__ = 'SYJ'
import requests,arrow,yaml,sys,random,base64,os,paramiko,re
from functools import wraps
import configparser,inspect
import json
import pytest,allure
import logging,os,excel,ddt
from common.loginuen import uenpay
from common.log import Log
from common.orc import Uenoracle
from common.YamlRead import HandleYaml

class Publick_G(object):
    '''公用方法调用'''
    # data = HandleYaml('WfbApp', 'app_config', 'Test_Apilogin')
    # '''获取当前类的方法名'''
    # def get_current_function_name(self):
    #     return inspect.stack()[1][3]
    # '''获得类名和当前函数名'''
    # classname = __name__  # 获得当前类名
    # currentfun = get_current_function_name(classname)  # 获得当前类下的函数名
    # '''读取yaml配置,项目传参'''
    # host = HandleYaml('WfbApp', 'app_config', 'config.yaml').get_data()['test_apilogin']['Host']
    # url = host + data.get_data()['' + str(classname) + '']['Url']

    def Msg(self,type,phoneNumber,appname):
        '''发送短信公用方法
        :type:100001(注册请求),100002(忘记密码请求)
        :phoneNumber:使用的手机号码'''
        host=HandleYaml(appname,'app_config','config.yaml').get_data()['test_apilogin']['Host']
        # print (host)
        uri=HandleYaml(appname,'app_config','test_SendMsgValidator').get_data()['Test_SendMsgValidator']['Url']
        # print (uri)
        url=host+uri
        AppKey=HandleYaml(appname,'app_config','config.yaml').get_data()['test_apilogin']['AppKey']
        headers={"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
                           "Accept-Language": "zh-Hans-CN;q=1",
                           "Accept-Encoding": "gzip, deflate",
                           "Content-Type": "application/json;charset=UTF-8"}
        body={"data": {"type": type, "phoneNumber": phoneNumber}, "meta": {"appKey": "vj5DYRpZ", "accessToken": "swUpGb3BTFih9KUzBdy21g", "clientName": "IOS_10.3.3_qsj", "clientVersion": "v1.0", "transCode": "1001", "transDate": "2018-5-17 10:50:00", "username": phoneNumber}}
        body["meta"]['appKey']=AppKey
        # print ('body-------------------------------------------------------------:%s'%body)
        req=requests.post(url,json=body,headers=headers)
        res=req.json()
        # print (res['meta']['accessToken'])
        msg=[]
        # msg.append(res['meta']['accessToken'])
        return msg

    def print_req(func):

        @wraps(func)  # <-----装饰器内部使用，修饰内置函数，需要参数为目标函数对象
        def with_logging(*args,**kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)
        return with_logging


    def randomPhoneNum(self):
        a=random.randint(1000,9999)
        phone='1371000'+str(a)
        return phone


    def picture_to_base64(self, picturepath):
        f = open(picturepath, 'rb')  # 二进制方式打开图文件
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()
        return ls_f


    def catch_Num(self,phonenum):
        '''抓取测试环境app验证码'''
        ssh = paramiko.SSHClient()  # 调用paramiko模块下的SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())  # 加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
        ssh.connect('192.168.1.232', 22, 'test', '123456')  # 连接远程主机，SSH端口号为22
        # command = 'tail -100 /tmp/rizhi'
        command= 'tail -500 /logs/ams/ams.log'
        stdin, stdout, stderr = ssh.exec_command(command)  # 执行命令
        logs = stdout.readlines()
        # print (logs)
        # print (type(logs[0]))
        # phone=re.findall('手机号：(.*?)',logs)
        # print (phone)
        yanzheng=[]
        for i in range(len(logs)):
            # print(logs[i].rstrip())
            # print (phonenum)
            phone = re.findall("手机号："+str(phonenum)+".*?验证码.*?(\d{6})", logs[i])
            # phone = re.findall("SmsOdanSignManageServiceImpl:105 - .*?(" + str(phonenum) + ".*?)\n", logs[i])
            if phone:
                # print(phone)
                yanzheng.append(phone[0])
        ssh.close()
        return yanzheng


    def catch_NumAgent(self, phonenum):
        '''抓取测试环境app验证码'''
        ssh = paramiko.SSHClient()  # 调用paramiko模块下的SSHClient()
        ssh.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())  # 加上这句话不用担心选yes的问题，会自动选上（用ssh连接远程主机时，第一次连接时会提示是否继续进行远程连接，选择yes）
        ssh.connect('192.168.1.200', 22, 'agent', '123456')  # 连接远程主机，SSH端口号为22
        # command = 'tail -100 /tmp/rizhi'
        command = 'tail -2000 /home/agent/logs/wfbs/wfbs-api/wfbs.log'
        stdin, stdout, stderr = ssh.exec_command(command)  # 执行命令
        logs = stdout.readlines()
        # print (logs)
        # print (type(logs[0]))
        # phone=re.findall('手机号：(.*?)',logs)
        # print (phone)
        yanzheng = []
        for i in range(len(logs)):
            # print(logs[i].rstrip())
            # print (phonenum)
            # phone = re.findall("手机号："+str(phonenum)+".*?验证码.*?(\d{6})", logs[i])
            phone = re.findall(""+str(phonenum)+".*(\d{6})", logs[i])
            if phone:
                # print(phone)
                yanzheng.append(phone[0])
        ssh.close()
        return yanzheng


    def getpost(self,url,**dataall):
        params=dataall.get('param')
        headers=dataall.get('headers')
        json=dataall.get('json')
        # req=requests.post('post',url,headers=headers,json=json)
        # res=req.text
        print (json)
        print (params)








if __name__ == '__main__':
    # A=Publick_G().Msg(100002,13761917640)
    # print (type(A.Msg(100002,13761917640)))
    # print (Publick_G().randomPhoneNum())
    # picturepath='H:\之前项目\pythonstudy\pythonstudy\python3\project\WfbApp\picture'
    # picture=os.path.join(picturepath,'TIM.png')
    A=Publick_G()
    # msg=A.Msg(100001,13761917640,'DailiApp')
    B=A.catch_NumAgent(13700006963)[0]
    print (B)
    # base=A.picture_to_base64(picture)
    # print (type(base))
    # s= bytes.decode(base)
    # print (s)
    # A = Publick_G().catch_Num(13761917640)
    # print (A)
    # yanzhengma = A[len(A) - 1]
    # # data={'json':'123123',
    # #       'headers':'token11111'}
    # #
    # # A.getpost('https://www.baidu.com/',**data)
    # # 验证码=A.catch_Num('13761917640')
    # # # print (len(验证码))
    # # # for i in range(len(验证码)):
    # # #     print (i)
    # # #     print (验证码[i])
    # # print (验证码[len(验证码)-1])
    # print ('验证码：{}'.format(A))


