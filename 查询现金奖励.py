#coding:utf8
import pymysql

global conn,cur,a,b,c,d
conn=pymysql.connect(host='192.168.1.132', port=3306, user='bbq', passwd='bbq123456', db='bbq_financz_test', charset='utf8')
cur=conn.cursor(pymysql.cursors.DictCursor)
def invest_id(fk_user_id):
    # sql="SELECT * FROM fiz_red_packet WHERE fk_user_id='"+str(fk_user_id)+"' AND fiz_red_packet.dc_category='10' AND dt_issue_time like '2017-07%'GROUP BY dt_create_time DESC ;"
    sql="SELECT * FROM fiz_red_packet WHERE fk_user_id='"+str(fk_user_id)+"' AND dc_category='10' AND fk_plan_invest_id IS NOT NULL ORDER BY dt_create_time DESC ;"
    cur.execute(sql)
    result=cur.fetchall()
    print ((len(result)))
    invest_id=[]
    r=[result[x]['fk_plan_invest_id'] for x in range(len(result)) if result[x]['fk_plan_invest_id']]
    for a in range(0,len(r)):
        # print (r[a])
        invest_id.append(r[a])
    # print invest_id[1]
    return invest_id
    # print (result[0]['fk_invest_id'])

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


def daishoubenxi():
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





if __name__ == '__main__':
    fk_user_id='a4eb8023-2b72-42ec-a4a1-a5ab320e6c2b'
    a = invest_id(fk_user_id)
    for x in range(0,len(a)):
        print (a[x])
        redpacket(a[x])
        c=redpacket(a[x])
        print (c)
        shouyi(c[0],c[1],c[2],c[3],c[4])
    # daishoubenxi()