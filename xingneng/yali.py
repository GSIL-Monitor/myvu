#coding = utf-8
from locust import HttpLocust, TaskSet, task
import json,requests,random



class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """

    def login(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
            "Origin": "http://192.168.1.133",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/json;charset=UTF-8"}
        body = {"data":
                    {"account": "18100000022", "password": "a111111"},
                "meta":
                    {"clientType": "0", "pageCode": "userSignIn"}
                }
        # req = self.client.post('/bbl-web/authenticate', data=body, headers=headers)
        # print (json.dumps(json.loads(req.content),ensure_ascii=False))
        # print (type(json.loads(req.content)))
        self.client.post('/bblc-web-v20/user/authenticate',headers=headers,json=body)
            # if R.status_code != 200:
            #     print ("failur")
            #     # R.failure('go wrong:'+(json.dumps(json.loads(R.content),ensure_ascii=False)))
            # else:
            #     print (R.content)
            #     R.success()

    def applogin(self):
        global token
        headers={"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
                 "Accept-Language": "zh-Hans-CN;q=1",
                 "Accept-Encoding": "gzip, deflate",
                 "Content-Type": "application/x-www-form-urlencoded"}
        body={"app_key":"KtASCNff",
              "cellphone":"18100000007",
              "password":"a111111",
              "pushId":"121c83f7601b4790a65",
              "secret_code":"22da848de43cc8cd893eae98ea519c18",
              "version":"2.6.1"}
        req=self.client.post("/bbl-app/user/sign_in",headers=headers,data=body)
        res=req.json()
        print (res["access_token"])
        token=res["access_token"]
        return token

    # @task
    # def chong(self):
    #     amount=random.randint(10,999)
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3230.0 Safari/537.36",
    #         "Origin": "http://192.168.1.133",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Content-Type": "application/json;charset=UTF-8"}
    #     body = {"data": {"tranAmount": amount, "payPassword": "111111", "configPassword": ""},
    #             "meta": {"clientType": "0", "pageCode": "userQuickRecharge"}}
    #     # req = self.client.post('/bbl-web/authenticate', data=body, headers=headers)
    #     # print (json.dumps(json.loads(req.content),ensure_ascii=False))
    #     # print (type(json.loads(req.content)))
    #     self.client.post('/bblc-web-v20/recharge/submit', headers=headers, json=body)

    @task
    def appchong(self):
        amount = random.randint(10, 999)
        headers = {"User-Agent": "JPjbp/2.6.1 (iPhone; iOS 10.2; Scale/3.00)",
                   "Accept-Language": "zh-Hans-CN;q=1",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/x-www-form-urlencoded"}
        body={"meta":{"appKey":"vj5DYRpZ","accessToken":"NYNmefhpS5ySiid3WSET6A"},"data":{"agentOrderId":400}}
        body['meta']['accessToken'] = self.accessToken['meta']['accessToken']
        self.client.post('/wfbs-api/order/findOderDetail',headers=headers,data=body)




class WebsiteUser(HttpLocust):
    host = 'http://192.168.1.232'
    task_set = UserBehavior

    min_wait = 100

    max_wait = 100

