# coding = utf-8
from locust import HttpLocust, TaskSet, task
import random
import os, sys, requests, json, random

print(sys.path)
sys.path.append('H:\之前项目\pythonstudy\pythonstudy\python3')
from common.orc import Uenoracle
import subprocess, queue
ora=Uenoracle(project='DailiApp', configname='app_config', confignYaml='config.yaml')

class UserBehavior(TaskSet):

    def on_start(self):

        """ on_start is called when a Locust start before any task is scheduled """
        # pass
        # filePath = 'H:\之前项目\pythonstudy\pythonstudy\python3\project1\project_config'
        # fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        # yamlPath = os.path.join(filePath, 'config.yaml')
        # '''读取用例文件的路径以及名称'''
        # script_path = os.path.realpath(__file__)
        # filename = os.path.split(script_path)[1]
        headers = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
                   "Accept-Language": "zh-Hans-CN;q=1",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/json;charset=UTF-8"}
        # phoneNumber=['13764906431','13760000062','13760000080','13760000091','13760000092','13760000098','13000000099']
        self.a = self.locust.queueData.get()
        print (self.a)
        # # phoneNumber=self.oracle_select()
        # orgidlist=['3236','3297','3111']
        randomnum = random.randint(0, 2)
        # print ("randomnum:%s"%(randomnum))
        # self.a=phoneNumber[int(randomnum)]
        print("on_start_self.a:%s"%(self.a))
        # self.a = self.a[int(randomnum)]
        # self.a = phoneNumber[i]
        AppLoginUrl = 'http://192.168.1.81:8082/wfbs-api/user/login'
        AppLoginBody = {"data": {"password": "qINjFwzdNqgKFBYHXGkDeg==", "phoneNumber": self.a},
                        "meta": {"appKey": "vj5DYRpZ", "accessToken": "mallList", "clientName": "IOS_10.3.3_qsj",
                                 "clientVersion": "1.1.1", "transCode": "1001", "transDate": "20180-5-17 10:50:00",
                                 "username": self.a}}
        req = requests.post(AppLoginUrl, json=AppLoginBody, headers=headers)
        res = req.json()
        self.accessToken = res["meta"]["accessToken"]
        # self.orgid=orgidlist[int(random.randint(0,2))]
        # print (self.orgid)
        # print(res)
        # print(res["meta"]["accessToken"])
        # self.a = self.locust.queueData.get()
    #
    # def oracle_select(self):
    #     orcQ = Uenoracle(project='WfbApp', configname='app_config', confignYaml='config.yaml')
    #     sql = "select c.ORG_ID,a.IS_AUTH,b.USER_NAME,a.* from agent_register_user_detail a  join AGENT_REGISTER_USER b on a.AGENT_REGISTER_USER_ID=b.AGENT_REGISTER_USER_ID and a.USER_REAL_NAME='盛轶骏' left join AGENT_ORG c on a.AGENT_REGISTER_USER_ID=c.AGENT_REGISTER_USER_ID order by a.CREATE_TIME desc"
    #     phonelist = []
    #     orgid = orcQ.orc_select(sql)
    #     for a in range(len(orgid)):
    #         # print (orgid[a-1])
    #         phonelist.append(orgid[a - 1]['USER_NAME'])
    #     # print(phonelist)
    #     return phonelist
    #
    # @staticmethod
    # def wfbs_login():
    #     headers = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
    #                "Accept-Language": "zh-Hans-CN;q=1",
    #                "Accept-Encoding": "gzip, deflate",
    #                "Content-Type": "application/json;charset=UTF-8"}
    #     AppLoginUrl = 'http://192.168.1.232/wfbs-api/user/login'
    #     AppLoginBody = {"data": {"password": "qINjFwzdNqgKFBYHXGkDeg==", "phoneNumber": 13764906431},
    #                     "meta": {"appKey": "vj5DYRpZ", "accessToken": "mallList", "clientName": "IOS_12_qsj",
    #                              "clientVersion": "v1.0", "transCode": "1001", "transDate": "20180-5-17 10:50:00",
    #                              "username": 13761917640}}
    #     req = requests.post(AppLoginUrl, json=AppLoginBody, headers=headers)
    #     res = req.json()
    #     accessToken = res["meta"]["accessToken"]
    #     print(res)
    #     print(res["meta"]["accessToken"])
    #     return accessToken
    #
    @task
    def findDeviceById(self):
        headers1 = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
                    "Accept-Language": "zh-Hans-CN;q=1",
                    "Accept-Encoding": "gzip, deflate",
                    "Content-Type": "application/json;charset=UTF-8"}
        # body = {"data": {"deviceTypeExtendId": 1},
        #         "meta": {"appKey": "vj5DYRpZ", "accessToken": "WHDomnSBRni_W-q41aJ7xQ", "clientName": "IOS_12.6_qsj",
        #                  "clientVersion": "v1.0", "transCode": "1001"}}
        body={"meta":{"appKey":"vj5DYRpZ","accessToken":"7WX3T1FdQdW6IdATuC57-g","username":"18001700189"},"data":{}}
        body['meta']['accessToken'] = self.accessToken
        self.client.request(method='POST', url='/wfbs-api/test/testDb', headers=headers1,
                            data=json.dumps(body))
    #
    # @task(3)
    # def selectUserInfo(self):
    #     headers1 = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
    #                 "Accept-Language": "zh-Hans-CN;q=1",
    #                 "Accept-Encoding": "gzip, deflate",
    #                 "Content-Type": "application/json;charset=UTF-8"}
    #     body = {"data": {"phoneNumber": self.a}, "page": {"pageNumber": 1, "pageSize": 10},
    #             "meta": {"appKey": "vj5DYRpZ", "accessToken": "vTHOzgWETvieu_OInqVIAg", "clientName": "IOS_12_qsj",
    #                      "clientVersion": "v1.0", "transCode": "1001", "transDate": "2018-5-17 10:50:00",
    #                      "username": 13764906431}}
    #     body['meta']['accessToken'] = self.accessToken
    #     self.client.request(method='POST', url='/wfbs-api/userInfo/selectUserInfo', headers=headers1,
    #                         data=json.dumps(body))
    #
    # @task(1)
    # def selectObjList_Agent(self):
    #     headers1 = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
    #                 "Accept-Language": "zh-Hans-CN;q=1",
    #                 "Accept-Encoding": "gzip, deflate",
    #                 "Content-Type": "application/json;charset=UTF-8"}
    #     body = {"data": {"orgId": self.orgid, "userId": 1095, "userType": 1, "userName": ""},
    #             "page": {"pageNumber": 0, "pageSize": 10},
    #             "meta": {"appKey": "vj5DYRpZ", "accessToken": "BiDvpgLOR2-dT02PwL7H0g", "clientName": "IOS_12_qsj",
    #                      "clientVersion": "v1.0"}}
    #     body['meta']['accessToken'] = self.accessToken
    #     self.client.request(method='POST', url='/wfbs-api/serve/selectObjList', headers=headers1, data=json.dumps(body))
    #
    # @task(1)
    # def selectObjList_Shop(self):
    #     headers1 = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
    #                 "Accept-Language": "zh-Hans-CN;q=1",
    #                 "Accept-Encoding": "gzip, deflate",
    #                 "Content-Type": "application/json;charset=UTF-8"}
    #     body = {"data": {"orgId": self.orgid, "userId": 1095, "userType": 2, "userName": ""},
    #             "page": {"pageNumber": 0, "pageSize": 10},
    #             "meta": {"appKey": "vj5DYRpZ", "accessToken": "BiDvpgLOR2-dT02PwL7H0g", "clientName": "IOS_12_qsj",
    #                      "clientVersion": "v1.0"}}
    #     body['meta']['accessToken'] = self.accessToken
    #     with self.client.request(method='POST', url='/wfbs-api/serve/selectObjList', headers=headers1,
    #                              data=json.dumps(body)) as response:
    #         if response.status_code != 200:
    #             print(response.json())
    #             response.failure()
    #         # else:
    #         #     response.success()
    #
    # @task(5)
    # def selectServeInfo(self):
    #     headers1 = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS_12; Scale/3.00)",
    #                 "Accept-Language": "zh-Hans-CN;q=1",
    #                 "Accept-Encoding": "gzip, deflate",
    #                 "Content-Type": "application/json;charset=UTF-8"}
    #     body = {"meta":{"appKey":"vj5DYRpZ","clientVersion":"1.0.3","clientName":"IOS_12.0_qsj","username":"13761917640","accessToken":"a91cEz4qSp-VB7lz4BOE8w","transCode":"100100401","transDate":"20180802112823"},"data":{"orgId":self.orgid}}
    #     body['meta']['accessToken'] = self.accessToken
    #     with self.client.request(method='POST', url='/wfbs-api/serve/selectServeInfo', headers=headers1,
    #                              data=json.dumps(body)) as response:
    #         if response.status_code != 200:
    #             print(response.json())
    #             response.failure()
    #
    # @task
    # def insert1_data(self):
    #     '''插入数据'''
    #     print(self.a)
    #     # id=self.a[i]
    #     # rownumsql="select PURCHASE_CASHBACK_RECORD_ID from purchase_cashback_record  where ROWNUM=1 order by PURCHASE_CASHBACK_RECORD_ID desc "
    #     # rownum=ora.orc_select(rownumsql)[0]['PURCHASE_CASHBACK_RECORD_ID']+1
    #     # print (rownum)
    #     # print ("insert into purchase_cashback_record values (129,3222,3333,150,5,systimestamp,NULL,NULL,NULL,NULL,NULL,01)")
    #     # randomnum=random.randint(1,100000)
    #     sql="insert into purchase_cashback_record values (SEQ_PURCHASE_CASHBACK_RECORD.nextval,3222,3333,150,5,systimestamp,NULL,NULL,NULL,NULL,NULL,01)"
    #     print (sql)
    #     res=ora.insert_sql(sql)
    #     # print (res)
    #
    # @task
    # def insert_data(self):
    #     '''插入交易'''
    #     print(self.a)
    #     rownumsql="select * from POS_TRADE order by TRADE_DATE desc "
    #     trade_no=int(ora.orc_select(rownumsql)[0]['TRADE_NO'])+1
    #     print (trade_no)
    #     # print ("insert into purchase_cashback_record values (129,3222,3333,150,5,systimestamp,NULL,NULL,NULL,NULL,NULL,01)")
    #     # randomnum=random.randint(1,100000)
    #     sql="INSERT INTO POS_TRADE(trade_id,trade_no, trade_type, card_category, trade_date, trade_status,txn_code,device_type, uen_answer_code, uen_answer_info, old_trade_seq_no, old_date_domain, old_trade_code,old_trade_date, old_trade_time, old_sys_tracking_no, old_batch_id, sys_tracking_no, retrieval_ref_no,domain_8583_7, old_pos_seq_no, pos_trade_no, pos_terminal_shop_no, pos_terminal_no, pos_terminal_batch_no,pos_auth_code,old_sys_ref_no, sys_ref_no, out_server, out_trade_code,channel_org_name, channel_id,third_trade_date, third_trade_time, third_seq_no, third_check_flag,third_shop_no, third_terminal_no,third_batch_no, third_author_code,third_operator, third_return_code, third_sys_ref_no, transfer_reserved,accept_reserved, id_no, account_no,bank_card_name, card_no, card_seq, card_type, card_expiry_date,credit_card_no, transfer_card_no, currency, trade_amount, return_amount, fee, cost_fee, shop_fee_id,shop_fee, input_mode, org_id, shop_id, branch_id, shop_name, pos_cnd, route_flag, coord_x, coord_y,trade_province, trade_city,trade_address, risk_flg,trade_time,exp_business_id,big_shop_no,big_shop_name,parent_org_ids,shop_no,channel_fee_id,f40,psam_no,profit_type,business_fee_id) values(SEQ_POS_TRADE.NEXTVAL,'" + str(trade_no) + "', '82', '1', systimestamp, '05','kb3303', null, 'GE','未知错误', null,null, null, null, null,null, null, null, null, null, null,null, null, '10003099', null, null,null,null, null, null,'海科总部(线上)', '1090', null,  null,null, null,null, '20004621', null, null,null, null, null,null, null, null, '3093','建设银行_龙卡通', '6217001180007802179', null, '0', '2710', '01050000', null, '156',15.00, null, 0.00, 0.0900, 76445, 0.50, '051', 3297, 36672, 36652,null, 'qsj', null, '31.183804', '121.423593', '上海市', '上海市','上海市徐汇区桂林路', null,null,43,'201710010000731','201710010000731',',3111,3236,3297,','018061114592251',1193,null,'D040000000012212','3',43)"
    #     # print (sql)
    #     res=ora.insert_sql(sql)
    #
    # @task
    # def insert_data1(self):
    #     '''插入交易'''
    #     print (self.a)
    #     rownumsql="select * from POS_TRADE order by TRADE_DATE desc "
    #     trade_no=int(ora.orc_select(rownumsql)[0]['TRADE_NO'])+1
    #     print (trade_no)
    #     # print ("insert into purchase_cashback_record values (SEQ_PURCHASE_CASHBACK_RECORD.nextval,3222,3333,150,5,systimestamp,NULL,NULL,NULL,NULL,NULL,01)")
    #     # randomnum=random.randint(1,100000)
    #     sql="INSERT INTO POS_TRADE(trade_id,trade_no, trade_type, card_category, trade_date, trade_status,txn_code,device_type, uen_answer_code, uen_answer_info, old_trade_seq_no, old_date_domain, old_trade_code,old_trade_date, old_trade_time, old_sys_tracking_no, old_batch_id, sys_tracking_no, retrieval_ref_no,domain_8583_7, old_pos_seq_no, pos_trade_no, pos_terminal_shop_no, pos_terminal_no, pos_terminal_batch_no,pos_auth_code,old_sys_ref_no, sys_ref_no, out_server, out_trade_code,channel_org_name, channel_id,third_trade_date, third_trade_time, third_seq_no, third_check_flag,third_shop_no, third_terminal_no,third_batch_no, third_author_code,third_operator, third_return_code, third_sys_ref_no, transfer_reserved,accept_reserved, id_no, account_no,bank_card_name, card_no, card_seq, card_type, card_expiry_date,credit_card_no, transfer_card_no, currency, trade_amount, return_amount, fee, cost_fee, shop_fee_id,shop_fee, input_mode, org_id, shop_id, branch_id, shop_name, pos_cnd, route_flag, coord_x, coord_y,trade_province, trade_city,trade_address, risk_flg,trade_time,exp_business_id,big_shop_no,big_shop_name,parent_org_ids,shop_no,channel_fee_id,f40,psam_no,profit_type,business_fee_id) values(SEQ_POS_TRADE.NEXTVAL+1000,'" + str(trade_no) + "', '82', '1', systimestamp, '05','kb3303', null, 'GE','未知错误', null,null, null, null, null,null, null, null, null, null, null,null, null, '10003099', null, null,null,null, null, null,'海科总部(线上)', '1090', null,  null,null, null,null, '20004621', null, null,null, null, null,null, null, null, '3093','建设银行_龙卡通', '6217001180007802179', null, '0', '2710', '01050000', null, '156',15.00, null, 0.00, 0.0900, 76445, 0.50, '051', 3297, 36672, 36652,null, 'qsj', null, '31.183804', '121.423593', '上海市', '上海市','上海市徐汇区桂林路', null,null,43,'201710010000731','201710010000731',',3111,3236,3297,','018061114592251',1193,null,'D040000000012212','3',43)"
    #     print (sql)
    #     res=ora.insert_sql(sql)
    #
    # @task
    # def search_data(self):
    #     '''交易汇总'''
    #     print (self.a)
    #     sql="select pt.trade_id ,decode(pt.risk_flg, '0','GE', pt.uen_answer_code) uen_answer_code,pt.third_return_code,decode(pt.risk_flg, '0','交易请求超时', pt.uen_answer_info) uen_answer_info,cs.shop_name,cs.shop_no,cs.apply_name,co.org_code,co.org_name,pt.psam_no dev_serial_no,pt.trade_date,ccw.phone_no,pt.trade_type,pt.card_no,pt.trade_amount, decode(pt.risk_flg, '0', '05', pt.trade_status) trade_status,pt.card_type, pt.card_category cardCategory,pt.bank_card_name,pt.FEE,pt.trade_no,decode(pt.coupon_id,null,'0','1') coupon_trade,cbf.fee_alias from pos_trade_his pt inner join (select org_id,org_code,org_name from core_organization start with org_id = 58252 connect by prior org_id = ORG_PARENT_ID) co on pt.org_id = co.org_id left join core_shop cs on pt.shop_id = cs.shop_id left join core_contact_way ccw on cs.contact_id=ccw.contact_id left join core_business_fee cbf on pt.business_fee_id = cbf.business_fee_id where 1=1 ORDER BY pt.TRADE_DATE DESC"
    #     res=ora.orc_select(sql)
    #     # print(res)
    #
    #
    # @task
    # def search1_data(self):
    #     '''交易分页'''
    #     print (self.a)
    #     sql="select pt.trade_id ,decode(pt.risk_flg, '0','GE', pt.uen_answer_code) uen_answer_code,pt.third_return_code,decode(pt.risk_flg, '0','交易请求超时', pt.uen_answer_info) uen_answer_info,cs.shop_name,cs.shop_no,cs.apply_name,co.org_code,co.org_name,pt.psam_no dev_serial_no,pt.trade_date,ccw.phone_no,pt.trade_type,pt.card_no,pt.trade_amount, decode(pt.risk_flg, '0', '05', pt.trade_status) trade_status,pt.card_type, pt.card_category cardCategory,pt.bank_card_name,pt.FEE,pt.trade_no,decode(pt.coupon_id,null,'0','1') coupon_trade,cbf.fee_alias from pos_trade_his pt inner join (select org_id,org_code,org_name from core_organization start with org_id = 58252 connect by prior org_id = ORG_PARENT_ID) co on pt.org_id = co.org_id left join core_shop cs on pt.shop_id = cs.shop_id left join core_contact_way ccw on cs.contact_id=ccw.contact_id left join core_business_fee cbf on pt.business_fee_id = cbf.business_fee_id where 1=1 ORDER BY pt.TRADE_DATE DESC"
    #     # print (sql)
    #     res=ora.orc_select(sql)
    #     # print(res)
    #
    # @task
    # def search2_data(self):
    #     '''商户分页'''
    #     print (self.a)
    #     sql="SELECT sh.shop_id id,sh.data_version version, org.org_code orgCode,org.org_name orgName,sh.shop_no shopNo,sh.parent_shop_id parentShopId,sh.shop_code shopCode,sh.shop_name shopName,sh.state freezeStatus,sh.remark remark,org.short_name orgShortName,sh.org_id orgId,cw.contact_man contactMan,cw.phone_no phoneNo,sh.cert_no certNo,sh.biz_scope bizScope,a.update_time bindingCardTime,bc.od_name odName,a.account_name accountName,a.bank_name bankName,sh.credit_level creditLevel,org.org_category orgCategory ,sh.create_time applyDate FROM core_shop sh LEFT JOIN core_organization org ON sh.org_id=org.org_id LEFT JOIN core_contact_way cw ON sh.contact_id=cw.contact_id LEFT JOIN core_account a ON sh.account_id=a.account_id LEFT JOIN core_address ad ON sh.addr_id=ad.addr_id LEFT JOIN base_customer bc on sh.shop_id = bc.shop_id inner join (select org_id  from core_organization start with org_id = 58252 connect by prior org_id = ORG_PARENT_ID) d on d.org_id = sh.org_id"
    #     res=ora.orc_select(sql)
    #     # print(res)
    #
    # @task
    # def search3_data(self):
    #     '''提现分页'''
    #     print (self.a)
    #     sql="SELECT sh.shop_id id,sh.data_version version, org.org_code orgCode,org.org_name orgName,sh.shop_no shopNo,sh.parent_shop_id parentShopId,sh.shop_code shopCode,sh.shop_name shopName,sh.state freezeStatus,sh.remark remark,org.short_name orgShortName,sh.org_id orgId,cw.contact_man contactMan,cw.phone_no phoneNo,sh.cert_no certNo,sh.biz_scope bizScope,a.update_time bindingCardTime,bc.od_name odName,a.account_name accountName,a.bank_name bankName,sh.credit_level creditLevel,org.org_category orgCategory ,sh.create_time applyDate FROM core_shop sh LEFT JOIN core_organization org ON sh.org_id=org.org_id LEFT JOIN core_contact_way cw ON sh.contact_id=cw.contact_id LEFT JOIN core_account a ON sh.account_id=a.account_id LEFT JOIN core_address ad ON sh.addr_id=ad.addr_id LEFT JOIN base_customer bc on sh.shop_id = bc.shop_id inner join (select org_id  from core_organization start with org_id = 58252 connect by prior org_id = ORG_PARENT_ID) d on d.org_id = sh.org_id"
    #     res=ora.orc_select(sql)
    #     # print(res)
    #
    # @task
    # def search4_data(self):
    #     '''机构分页'''
    #     print (self.a)
    #     sql="select org.org_id id,org.data_version version, org.salesman salesman,org.org_name orgName,org.ind_reg_nam indRegNam,org.org_code orgCode,org.ORG_TYPE orgType,org.apply_date applyDate,org.state freezeStatus,org.short_name shortName,parentorg.org_code parentOrgCode,parentorg.org_name parentOrgName,org.update_time lastUpdateTime,bo.user_really_name updateUserName,org.org_category orgCategory, rate.month_settle_rate dockingType from core_organization org LEFT JOIN base_constant cl ON org.state=cl.constant_id LEFT JOIN core_contact_way cw ON org.contact_id=cw.contact_id LEFT JOIN core_account a ON org.account_id=a.account_id LEFT JOIN base_bank_info bb ON a.bank_no=bb.bank_no LEFT JOIN core_address ad ON org.addr_id=ad.addr_id LEFT JOIN core_organization parentorg on org.org_parent_id=parentorg.org_id  LEFT JOIN base_user bo on org.update_user = bo.user_id  LEFT JOIN core_org_settle_rate rate on org.org_id = rate.org_id where org.data_status = '1' order by org.create_time desc"
    #     res=ora.orc_select(sql)
    #     # print(res)
    #
    # @task
    # def search5_data(self):
    #     '''商户分页2'''
    #     print (self.a)
    #     sql="SELECT sh.shop_id id,sh.data_version version, org.org_code orgCode,org.org_name orgName,sh.shop_no shopNo,sh.parent_shop_id parentShopId, sh.shop_code shopCode,sh.shop_name shopName,sh.state freezeStatus,sh.remark remark,org.short_name orgShortName,sh.org_id orgId,cw.contact_man contactMan,cw.phone_no phoneNo,sh.cert_no certNo,sh.biz_scope bizScope,a.update_time bindingCardTime,bc.od_name odName,a.account_name accountName,a.bank_name bankName,sh.credit_level creditLevel,org.org_category orgCategory ,sh.create_time applyDate FROM core_shop sh LEFT JOIN core_organization org ON sh.org_id=org.org_id LEFT JOIN core_contact_way cw ON sh.contact_id=cw.contact_id LEFT JOIN core_account a ON sh.account_id=a.account_id LEFT JOIN core_address ad ON sh.addr_id=ad.addr_id  LEFT JOIN base_customer bc on sh.shop_id = bc.shop_id	WHERE sh.data_status = '1' order by sh.create_time desc"
    #     res=ora.orc_select(sql)
        # print(res)
    #
    # @task
    # def register1(self):
    #     # i=1
    #     # self.a=self.locust.queueData.get()
    #
    #     # print(i)
    #     # i += 1
    #     print("self.a:%s" % (self.a))
        # try:
        #     data = self.locust.queueData.get()  #获取队列里的数据
        #     print("register1:%s"%(data))
        # except queue.Empty:                     #队列取空后，直接退出
        #     print('no data exist')
        #     exit(0)
        # self.locust.queueData.put_nowait(self.a)

    # @task
    # def register2(self):
    #     # i=1
    #     self.a = self.locust.queueData.get()
    #
    #     # print(i)
    #     # i += 1
    #     print("register2:%s" % (self.a))
    #     self.locust.queueData.put_nowait(self.a)
    #     try:
    #         data = self.locust.queueData.get()  #获取队列里的数据
    #         print("register1:%s"%(data))
    #     except queue.Empty:                     #队列取空后，直接退出
    #         print('no data exist')
    #         exit(0)


class WebsiteUser(HttpLocust):
    host = 'http://192.168.1.81:8082'
    queueData = queue.Queue(maxsize=0)  # 队列实例化
    # phoneNumber = ['13700008838', '15922220012', '13770000001', '13760000027', '13760000062', '13700002298', '13700005414', '13700004929', '13700003784', '13700009140', '13700009350', '13760000026', '13760000025', '13760000090', '18000000001', '13700001629', '13700004338', '13700004161', '13700001590', '13700001596', '13700003717', '13700007345', '13700002412', '13700008843', '13700002782', '13700003602', '13700001035', '13700007591', '13000000022', '13764906433', '13000000088', '13000000099', '13760000098', '13760000092', '13760000091', '13760000080', '13700001055', '13000000021', '13764906434', '13760000002', '13764906432', '13761917640', '13700008839']
    phoneNumber=['13764906431','18000000002']
    for i in range(len(phoneNumber)):
        phone=phoneNumber[i-1]
        queueData.put_nowait(phone)
    # num=[]
    # i=0
    # # queueData = queue.Queue(maxsize=5)  # 队列实例化
    # while i <= 100:
    #     queueData.put_nowait(i)
    #     i +=1
    # print (num)
    # queueData.put_nowait(num)




    task_set = UserBehavior

    min_wait = 0

    max_wait = 1


if __name__ == '__main__':
    subprocess.Popen('locust -f H:\之前项目\pythonstudy\pythonstudy\python3\\xingneng\wfbsce.py', shell=True)
