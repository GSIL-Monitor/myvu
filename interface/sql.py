#coding:utf8
import pymysql

global conn,cur,a,b,c,d
conn=pymysql.connect(host='127.0.0.1', port=3306, user='alca', passwd='111111', db='autoline', charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)

class sql():
    def invest_id(ziduan,phone):
        # sql="SELECT * FROM fiz_red_packet WHERE fk_user_id='"+str(fk_user_id)+"' AND fiz_red_packet.dc_category='10' AND dt_issue_time like '2017-07%'GROUP BY dt_create_time DESC ;"
        sql="select b.vc_name as '投资人',b.vc_cellphone as '电话',b.pk_id,a.nb_freeze_amount,a.nb_total_interest,a.nb_amount,a.nb_loan_amount,a.dt_create_time from fiz_dmd_balance a,fiz_user b where a.fk_user_id=b.pk_id and b.pk_id=(select pk_id from fiz_user r where vc_cellphone='"+str(phone)+"') order by dt_create_time DESC "
        cur.execute(sql)
        result=cur.fetchall()
        # print ((len(result)))
        list=[]
        r=[result[x][''+str(ziduan)+''] for x in range(len(result)) if result[x][''+str(ziduan)+'']]
        for a in range(0,len(r)):
            # print (r[a])
            list.append(r[a])
        list1 = 0
        for x in range(0, len(list)):
            # print(list[x])
            list1 += list[x]
        print(list1)
        return list1
        # print (result[0]['fk_invest_id'])

    def dongjie(ziduan,sqll):
        # sql = "select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('00','20')"
        sql=sqll
        cur.execute(sql)
        result = cur.fetchall()
        # print((len(result)))
        list = []
        r = [result[x][''+str(ziduan)+''] for x in range(len(result)) if result[x][''+str(ziduan)+'']]
        for a in range(0, len(r)):
            # print (r[a])
            list.append(r[a])
        # print (list)
        list1=0
        for x in range(0,len(list)):
            # print (list[x])
            list1 +=list[x]
        print (list1)
        return list1


    def redpacket(investid):
        # global a,b,c,d
        sql='SELECT l.nb_amount,s.nb_amount,l.vc_remark,r.* FROM fiz_red_packet l,fiz_plan r,fiz_plan_invest s WHERE l.fk_plan_invest_id=s.pk_id and s.fk_plan_id=r.pk_id and l.fk_plan_invest_id="'+str(investid)+'";'
        cur.execute(sql)
        result=cur.fetchall()
        # print (result[0])
        # print ("收益：%s"
        #        "投资金额：%s"
        #        "投资期限：%s"
        #        "投资类型：%s"%(result[0]['nb_amount'],result[0]['s.nb_amount'],result[0]['nb_period'],result[0]['dc_period_type']))
        a=result[0]['nb_amount']
        b=result[0]['s.nb_amount']
        c=result[0]['nb_period']
        d=result[0]['dc_period_type']
        e=result[0]['vc_remark']
        return a,b,c,d,e
        # print ("收益：%s  投资金额：%s  投资期限：%s  投资类型：%s"%(int(result['nb_amount']),int(result['s.nb_amopunt']),int(result['dc_period']),int(result['dc_period_type'])))

    def shouyi(a,b,c,d,e):
        # print (a)
        # print (b)
        # print (c)
        # print (d)
        # print (e)
        yue=float(b)*float(c)/365*0.005
        ji=float(b)*float(c)/365*0.01
        bannian=float(b)*float(c)/365*0.015
        nian=float(b)*float(c)/365*0.02
        Yue=float(b)*float(c)/12*0.005
        Ji=float(b)*float(c)/12*0.01
        Bannian=float(b)*float(c)/12*0.015
        Nian=float(b)*float(c)/12*0.02
        if d=="00":
            if '首投' in e:
                print(a, b, c, d, e)
                print("首投",10)
                print('----------------------------------')
            elif 0<=c<28:
                print(a, b, c, d, e)
                print ("新手标",yue)
                print ('----------------------------------')
            elif 28<=c<89:
                print(a, b, c, d, e)
                print ("月标",yue)
                print ('----------------------------------')
                # print (yue)
            elif  89<=c<180:
                print(a, b, c, d, e)
                print ("季度标",ji)
                print ('----------------------------------')
            elif 180<=c<360:
                print(a, b, c, d, e)
                print ("半年标",bannian)
                print ('----------------------------------')
            elif 360<=c:
                print(a, b, c, d, e)
                print ("年标",nian)
                print ('----------------------------------')
        else:
            if '首投' in e:
                print(a, b, c, d, e)
                print("首投",10)
                print('----------------------------------')
            elif 1<=c<3:
                print(a, b, c, d, e)
                print ("月标",Yue)
                print ('----------------------------------')
            elif 3<=c<6:
                print(a, b, c, d, e)
                print ("季度标",Ji)
                print ('----------------------------------')
            elif 6<=c<12:
                print(a, b, c, d, e)
                print ("半年标",Bannian)
                print ('----------------------------------')
            elif 12<=c:
                print(a, b, c, d, e)
                print ("年标",Nian)
                print ('----------------------------------')


    def daishoubenxi(self):
        # sql = "SELECT * FROM fiz_plan_invest WHERE fk_user_id='6e706599-5abd-4298-842a-cd766122b998'GROUP BY dt_create_time DESC;"
        sql = "SELECT * FROM fiz_plan_invest WHERE fk_user_id='a4eb8023-2b72-42ec-a4a1-a5ab320e6c2b'GROUP BY dt_create_time DESC;"
        cur.execute(sql)
        result = cur.fetchall()
        print (len(result))
        num = len(result)
        c = 0
        d = 0
        for a in range(0,num):
            nb_amount=result[a]['nb_amount']
            nb_profit=result[a]['nb_profit']
            print (nb_amount)
            print (nb_profit)
            c +=nb_amount
            d +=nb_profit
        print (c,d,c+d)


    def qianyueyonghu(self):
        '''查找签约用户进行登录参数化'''
        sql = "SELECT r.fk_rcmd_id,rcmded_user_id,l.vc_name,l.vc_account, l.vc_cellphone,r.first_date,r.dt_reward_end_date,r.reg_date from rpt_rcmd_rcmdedor r,fiz_user l WHERE r.rcmded_user_id=l.pk_id AND r.fk_rcmd_id=(select pk_id from fiz_user r where vc_cellphone='13761917640') and r.first_date is not null  order BY r.dt_create_time DESC "
        cur.execute(sql)
        result = cur.fetchall()
        print ((len(result)))
        list = []
        r = [result[x]['vc_cellphone'] for x in range(len(result)) if result[x]['vc_cellphone']]
        for a in range(0, len(r)):
            # print (r[a])
            list.append(r[a])
        list1 = 0
        return list
        # for x in range(0, len(list)):
            # print(list[x])
            # list1 += list[x]



if __name__ == '__main__':
    a = sql.dongjie('nb_amount',"select b.vc_name as '投资人',b.vc_cellphone as '电话',b.pk_id,a.nb_freeze_amount,a.nb_total_interest,a.nb_amount,a.nb_loan_amount,a.dt_create_time from fiz_dmd_balance a,fiz_user b where a.fk_user_id=b.pk_id order by dt_create_time DESC ")
    b=sql.dongjie('nb_loan_amount',"select b.vc_name as '投资人',b.vc_cellphone as '电话',b.pk_id,a.nb_freeze_amount,a.nb_total_interest,a.nb_amount,a.nb_loan_amount,a.dt_create_time from fiz_dmd_balance a,fiz_user b where a.fk_user_id=b.pk_id order by dt_create_time DESC ")
    c=sql.dongjie('nb_freeze_amount',"select b.vc_name as '投资人',b.vc_cellphone as '电话',b.pk_id,a.nb_freeze_amount,a.nb_total_interest,a.nb_amount,a.nb_loan_amount,a.dt_create_time from fiz_dmd_balance a,fiz_user b where a.fk_user_id=b.pk_id order by dt_create_time DESC ")
    d=sql.dongjie('nb_freeze_cash_amount',"select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('00','20');")
    e=sql.dongjie ('nb_freeeze_loan_amount',"select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('00','20');")
    f = sql.dongjie('nb_freeze_cash_amount',
                "select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('90');")
    print (a+b)
    print ("活期理财总额:%s"%(a+b-c+d+e+f))

    phoneNO='13761917640'
    A=sql.invest_id('nb_amount',phoneNO)
    B=sql.invest_id('nb_loan_amount',phoneNO)
    C=sql.invest_id('nb_freeze_amount',phoneNO)
    D=sql.dongjie('nb_freeze_cash_amount',"select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('00','20') and i.fk_user_id=(select pk_id from fiz_user r where vc_cellphone='"+str(phoneNO)+"');")
    E=sql.dongjie('nb_freeeze_loan_amount',"select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('00','20') and i.fk_user_id=(select pk_id from fiz_user r where vc_cellphone='"+str(phoneNO)+"');")
    F=sql.dongjie('nb_freeze_cash_amount',"select * from fiz_dmd_redeem_freeze_record i where i.dc_status in ('90') and i.fk_user_id=(select pk_id from fiz_user r where vc_cellphone='"+str(phoneNO)+"');")
    print ("个人活期理财总额:%s"%(A+B-C+D+E+F))
