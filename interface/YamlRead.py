#coding:utf8
__time__ = '2018/5/21 12:29'
__author__ = 'SYJ'

import yaml,os

class HandleYaml(object):
    def __init__(self, project,configname,confignYaml):
        # 获取当前文件路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy
        filePath = 'H:\之前项目\pythonstudy\pythonstudy\python3\project\\' + (project) + '\\' + (configname) + ''
        # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
        fileNamePath = os.path.split(os.path.realpath(__file__))[0]
        # 获取配置文件的路径 D:/WorkSpace/StudyPractice/Python_Yaml/YamlStudy\config.yaml
        # yamlPath = os.path.join(filePath, 'config.yaml')
        self.yamlPath = os.path.join(filePath, '' + (confignYaml) + '')
        # print (self.yamlPath)
        # self.data = self.get_data()

    def get_data(self):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        data = yaml.load(cont)
        f.close()
        # print (data)
        return data

    def  get_jsondata(self):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        p = yaml.load(cont)
        # print (p)
        jsonData = []
        for json in p.values():
            # print(json)
            if 'json' in json:
                # print (json)
                jsonData.append(json['json'])
        # print (jsonData)
        return jsonData


    def get_result(self,masterkey):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        p = yaml.load(cont)
        # print (p)
        result = []
        for json in p.values():
            # print(json)
            if ''+str(masterkey)+'' in json:
                # print (json)
                result.append(json[''+str(masterkey)+''])
        # print (jsonData)
        return result

    # @classmethod
    def make_data(self):
        # f = open(self.yamlPath, 'r', encoding='utf-8')
        # cont = f.read()
        # p = yaml.load(cont)
        postjson=[]
        assertresult=[]
        assertdatabase=[]
        introlist=[]
        # for content in p.values():
        #     print (content)
        # cont=HandleYaml('DailiApp','app_config','test_SendMsgValidator')
        jsondata=self.get_jsondata()        #调用自己类的实例要用self就可以了
        result=self.get_result('result')
        intro=self.get_result('intro')
        for i in range(len(jsondata)):
            postjson.append(jsondata[i])
            assertresult.append(result[i])
            introlist.append(intro[i])
        # print (jsondata)
        # print (result)
        postdata=[]
        introdata=[]
        for e in range(len(postjson)):
            postdata.append({'json':postjson[e],'result':assertresult[e]})
            introdata.append('intro='+str(introlist[e])+'')
        return postdata,introdata

    def make_testdata(self):
        f = open(self.yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        p = yaml.load(cont)
        postjson = []
        assertresult = []
        assertdatabase = []
        for content in p.values():
            print (content)
            if 'result' in content:
                print (content.keys())

                # for keys in content.keys():
                #     print (keys)





if __name__ == '__main__':
    # test = HandleYaml('DailiApp','app_config','Test_Register')
    # test = HandleYaml('DailiApp','app_config','config.yaml').get_data()
    # test_data = test.make_data()[0]
    # print(type(test_data))
    # print (test)
    # b={'accessToken':'qlcjr0X-TzqDNEh60MX6GQ'}
    # # print (test_data[0]['json']['meta']['accessToken'])
    # # b['accessToken']=p[0]['json']['meta']['accessToken']
    # test_data[0]['json']['meta']['accessToken']=b['accessToken']
    # print (test_data[0])
    # print (test.get_result())
    # a=HandleYaml('DailiApp','app_config','Test_Apilogin').make_testdata()
    # print (a)
    script_path = os.path.realpath(__file__)
    print (script_path)
    filename = os.path.split(script_path)[0]+'/config.yaml'
    print (filename.split("\\")[-1].split("/")[0])
