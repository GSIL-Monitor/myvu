#coding:utf-8
import requests
import re
import json
import time
ss=requests.session()

str_cookie='BAIDUID=80E67B8878193AAA204A25558D732CEF:FG=1; BIDUPSID=80E67B8878193AAA204A25558D732CEF; PSTM=1499066602; TIEBA_USERTYPE=0929173ec0eeca786ee7eb89; FP_UID=294f1cf82177de0194cb3b33c1fd07d6; bdshare_firstime=1500010193926; BDUSS=RmYkVGSmZWMGN2U2oza3l0TDZNZmJrcjhwTHdUR3NMUVp5NGw0ZkdIS2JNYnRaTVFBQUFBJCQAAAAAAAAAAAEAAADE3Xgzc3VtbWVyYmVycnlsb2wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJukk1mbpJNZRT; TIEBAUID=e7d5aa4e9f3ca8e5d7d493e7; FP_LASTTIME=1510637126563; MCITY=-%3A; 863559108_FRSVideoUploadTip=1; bottleBubble=1; STOKEN=12e4eec6df0cb5637b6c544010cf522840389c4440fd2a1327c04931a3523b2e; PSINO=5; H_PS_PSSID=1460_21091_17001_20930; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; fixed_bar=1; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1516347210,1516347231,1516592776,1516593838; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1516608283'
reg='([\s\S]*?)=([\s\S]*?);'
dict_cookie={}
for c in  re.findall(reg,str_cookie):
   dict_cookie[c[0]]=c[1]
   # print (c[0])
print ('dict_cookie:',dict_cookie)         ###cookie字符串转字典，也可以直接把cookie字符串携带在requests的请求头中实现登录

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
    ]
header={}
import random
dict_data={
'ie':'utf-8',
'kw':'雪鹰领主',
'fid':'17061897',
'tid':'3721320057',
'vcode_md5':'',
'floor_num':'2',
'rich_text':'1',
'quote_id':'106047109156',
'tbs':'a0ac8503750284f21516608278',
'content':'3333434343434那些杀不死我们的，终将使我们更',
'basilisk':'1',
'files':'[]',
    'mouse_pwd':'15,8,14,23,3,14,2,9,50,10,23,11,23,10,23,11,23,10,23,11,23,10,23,11,23,10,23,11,50,13,10,3,13,3,50,10,8,13,13,23,12,13,3,15166083024590',
    'mouse_pwd_t':'1516608302459',
    'mouse_pwd_isclick':'0',
    '__type__':'0',
    '_BSK':'JVwPUWcLBF83AFZzQzhHElBFIyI0RgFeUSNHUipmMiI4XjdHGmk/XS5dPCMNW09JKkc7USNwRWVyXBJSZwsEHHNNH30UfVQKSCoqLTNJGVYReEkWZR0ROT9UPxhAaQopVQVzZl8NfSYeHmsdXhFINzIbNgYnek1fakAAaE9/QBBCLA0DF2lZF1IkDENlciMzOl95T3AhNhIYVnJhVwMaR3oabARQYBgUPxgAESweERhyWwBpQ2BUXFhFf3cuVwBSEm8EF2cPZiQjRTVDEShwX08TOzYIXk9Fa19uFkRydhISMkNPZ0MVCX9XVSoPLwJZBQllJTtLEVhTZU4GPhUdPjBEORlWaScSEVYAdxkPBks5G30OXjZZKy0bTUEgAAYRZUcDblZ8QwFbS2cjaAdPFw94VhBzBX5jZwR8TUN4ZkdXFmoVQR8YHStbegZMdQsGe0xTAnVQRxNwRQBoVHxECF4Bd2ZvFEMBDnVVEX0QdGJ0BxRNH2szTlcJfTEFQVkMZQosB1xqGDMsCwRPZ0YWCX9XfQotAFQcSA50dWAFAUVLKEsENQdkanNnOQEAe2ZRV1JsdV4NG1p/HnMWH2MafX4YAA82VAgJIUQRZUMCI3wmRWl1NxRXDRwvBlUsWS8jOm8xI0V5LhpXH385Vw8QSXsYbgNOZQl2clwSUWcLBBp2QwVzQyBHElBFPz93ZjsVEm8QEmcPZCA+QyQiVjo3HBJWcTUIWFhFL0c8QQ18WysxDQRPI0NFRiAGHywEIBAcHQ4rMzVSWUdfPwJIMRkpIDReNR0fPSsNWV84OQNZQkUqRDBHGzQUKzEdABcsXkoHIRpQKgwpGERGCDc+PUwbG1AsCkNpXS8jJV8iFh8lKx4URzQ4Ck9LG2VFOloLMlk1cg4EETZeSkopF1ItTT8VQgULKTU7VwYVEm8JF2cPZmJhAWdfBnh1UVdSb3VeDR1acVU=',
'lp_type':'0',
'lp_sub_type':'0',
'new_vcode':'1',
'tag':'11',
'repostid':'106047109156',
'anonymous':'0',

}   ####抓包得到的
dict_data['kw']='雪鹰领主'  #重要，不能填错
dict_data['fid']='17061897'        #fid是贴吧什么时候建的，可以抓包也可以用上面的获取fid的接口得到，fid指的是贴吧是第多少个建的贴吧，数字越小，说明贴吧建的越早
dict_data['tbs']='a0ac8503750284f21516608278'   ##这个值是有生命周期的，用个天把时间没问题
dict_data['tid']='3721320057'    ##tid指的是主题帖子的id
dict_data['floor_num']='2'     ###这个不重要，随便多少都可以
dict_data['quote_id']='106092995926'      #用f12定位看以看到post_id字段，指的是层主帖子的id
dict_data['repostid']=dict_data['quote_id']
dict_data['content']='3333434343434那些杀不死我们的，终将使我们更'   #content顾名思义是回复的内容了，除了这几个外其他的data参数都可以不修改。


#获取fid的接口 ，吧name换成贴吧名字，复制到浏览器地址栏回车就ok了http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=%E6%B5%A0%E6%B0%B4%E4%BA%8C%E4%B8%AD

i=0

while(1):
    i=i+1
    try:
        header['User-Agent']=random.choice(user_agent_list)   ##习惯性的学爬虫来个随机换user-agent,但贴吧和知乎 这种都是基于账号追踪的，换ua和代理ip是没有任何作用的，逃避不了被识别为机器人
        header['Connection']='close'
        header.update({ 'Host':'tieba.baidu.com','Origin':'http://tieba.baidu.com','Referer':'https://tieba.baidu.com/p/3721320057'})

        dict_data['content']='晨曦魔力阿噗阿噗阿噗阿噗'+str(i)

        res=ss.post('http://tieba.baidu.com/f/commit/post/add',cookies=dict_cookie,data=dict_data,headers=header)
        # print (dict_data)
        res_content=res.content
        res_text=res.text.encode('gbk')
        # print (json.dumps(json.loads(res_text),ensure_ascii=False))
        # print (res_content)
        # res_json=res.json()
        # print (json.dumps(res_json))
        print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'  ',json.dumps(json.loads(res_content),ensure_ascii=False)) ###这样可以清楚的看到json里面的\u xxxx之类的对应的中文。

        if '"err_code":0' not in res.content:   ##errcode0表示回帖成功了

            i=i-1

        if '"err_code":220034' in res_content:
            time.sleep(300)     #说话太频繁，这时候不要太快回帖了，回了也没用，会连续返回errcode220034
        if '"need_vcode":0,' not in res_content:
            #print res_content
            print (u'需要验证码')
            time.sleep(180)         ###如果回复太快了会弹出验证码，等一段时间不回帖就好啦。
    except Exception as e:
        # i=i-1
        print (e)
    time.sleep(10)                   ##每隔10秒回帖