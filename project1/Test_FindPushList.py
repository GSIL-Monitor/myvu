#coding:utf8
__time__ = '2018/12/13 9:50'
__author__ = 'SYJ'

from ..WfbApp import *




@allure.feature("测试模块_Q刷伙伴App")
@pytest.mark.WfbApp       #标志WfbApp，跑jenkins时候只跑带有标识的
class Test_FindPushList():
    """
    推送信息列表
    """
    projectpath = os.path.realpath(__file__)
    ProjectName = os.path.split(projectpath)[0]
    Appname=ProjectName.split("\\")[-1].split("/")[0]
    data = HandleYaml(Appname,'app_config','Test_FindPushList')
    test_data=data.make_data()[0]
    intro_data = data.make_data()[1]



    '''获取当前类的方法名'''
    def get_current_function_name(self):
        return inspect.stack()[1][3]




    @classmethod
    def setup_class(cls):
        '''初始化数据'''
        global cf, pk_id, logger, fh, ch
        utc = arrow.now()
        # utc = utc.replace(days=-1)
        nowtime = utc.format('YYYY-MM-DD')
        cf = configparser.ConfigParser()
        cf.read("config.ini",encoding='utf-8')

        '''获得类名和当前函数名'''
        cls.classname = cls.__name__  # 获得当前类名
        cls.currentfun = cls.get_current_function_name(sys._getframe().f_code.co_name)  # 获得当前类下的函数名
        '''读取yaml配置,项目传参'''
        cls.host=HandleYaml(cls.Appname,'app_config','config.yaml').get_data()['test_apilogin']['Host']
        cls.url = cls.host+cls.data.get_data()[''+str(cls.classname)+'']['Url']
        cls.header = cls.data.get_data()[''+str(cls.classname)+'']['Header']

        '''读取用例文件的路径以及名称'''
        script_path = os.path.realpath(__file__)
        # print (script_path)
        filename = os.path.split(script_path)[1]
        # print ("filename:%s"%(filename))

        '''定义日志'''
        cls.log=LogManager('WfbApp').get_logger_and_add_handlers(log_level_int=1, is_add_stream_handler=True,  log_filename='test.log',log_file_size=10,formatter_template=2,log_path='H:/之前项目/pythonstudy/pythonstudy/python3/log')
        # cls.log=LogManager('WfbApp').get_logger_and_add_handlers(log_level_int=1, is_add_stream_handler=True,  log_filename='test.log',log_file_size=10,formatter_template=2,log_path='H:/之前项目/pythonstudy/pythonstudy/python3/log')
        cls.log.info('执行开始%s---------------------------------------'% format(cls.get_current_function_name(sys._getframe().f_code.co_name)))

        '''登录系统保持session'''
        # cls.username=cls.read['account']['username']
        # cls.password = cls.read['account']['password']
        requests.packages.urllib3.disable_warnings()
        # urllib3.disable_warnings()
        s = requests.session()
        cls.login=uenpay(s,cls.Appname)
        cls.accessToken=cls.login.applogin()
        # print(res)


        '''查询数据库用户信息,项目传参'''

        cls.Oracle=Uenoracle('WfbApp','app_config','Test_FindPushList')

        # '''前置登录获取token'''
        # s = requests.session()
        # cls.login = uenpay(s)
        # cls.token=cls.login.applogin()
        # print(cls.token)





    @classmethod
    def teardown_class(cls):
        '''关闭数据库'''
        # cls.conn.close()
        cls.log.info('执行结束%s---------------------------------------'% format(cls.get_current_function_name(sys._getframe().f_code.co_name)))


    @allure.story("推送信息列表")
    @allure.testcase("用例名：推送信息列表")
    @pytest.mark.parametrize('data',test_data,ids=intro_data)
    def test_api(self,data):
        """
        推送信息列表
        :param data:
        :return:
        """
        print(data)
        # 登录成功后替换config.yaml里的账号信息以及替换token进行后续接口操作
        self.log.info(json.dumps(data['json']))
        data['json']['meta']['accessToken'] = self.accessToken['meta']['accessToken']
        req = self.login.Uen('POST', url=self.url, param=data['json'], headers=self.header)
        self.log.debug(req)
        assert req['meta']['statusCode'] == data['result']






if __name__ == '__main__':
    # Test_SendMsgValidator()
    # print (__name__)
    pytest.main('-q Test_FindPushList.py')