#coding:utf8
__time__ = '2018/5/24 9:24'
__author__ = 'SYJ'

import json
from common.YamlRead import HandleYaml

data = HandleYaml('DailiApp', 'app_config', 'Test_Apilogin')
test_data = data.make_data()
data={"a":"2"}
def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):       # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False

if __name__ == "__main__":
    print (check_json_format("""{"a":1}"""))
    # print (check_json_format("""{'a':1}"""))
    # print (check_json_format({'a': 1}))
    print (check_json_format(test_data))
    print(check_json_format(data))