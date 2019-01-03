#coding=utf-8
import pymysql
from multiprocessing_log_manager import LogManager

logger = LogManager('logger_name').get_logger_and_add_handlers(log_level_int=1, is_add_stream_handler=True,  log_file_size=10,formatter_template=2)

logger.debug('hell')

logger.info('world')

def shouyi():
    print ("2222222")
    conn = pymysql.connect(host='192.168.1.132',user='bbq',passwd='bbq123456',port=3306,db='bbq_financz_test',charset='utf8')
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # print (cur)
    # cur=conn.cursor(cursor=pymysql)
    # sql = "SELECT * FROM fiz_plan_invest where fk_user_id = 'f2711cfc-666a-4550-b643-671207c531fd' GROUP BY dt_create_time DESC ;"
    cur.execute("SELECT * FROM fiz_plan_invest where fk_user_id = 'f2711cfc-666a-4550-b643-671207c531fd' GROUP BY dt_create_time DESC ;")
    result = cur.fetchall()
    # print (result)
    # for x in range(0,2):
    #     print (x)
    r = 0
    for x in range(0,len(result)):
        print (result[x]['nb_profit'])
        r +=result[x]['nb_profit']
    for x in range(0,len(result)):
        print (result[x]['nb_amount'])
        r +=result[x]['nb_amount']
    print ("所有收益为:%s"%(r))
    # print ("pk_id:%s"%(result['vc_sys_request_no']))

if __name__ == '__main__':
    # shouyi()
    # logger.info('world')
    A=[1,1,2]
    B=[2,2,3]
    A[0]=3
    print (A)

