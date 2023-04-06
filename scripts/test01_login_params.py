'''
定义接口测试用例
使用unittest
'''
import json

import requests
import unittest
from api.login import LoginAPI
from parameterized import parameterized


# 构造数据
def build_data():
    file = '../data/login.json'
    test_data = []
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        for case_date in json_data:
            account = case_date.get("account")
            password = case_date.get("password")
            status_code = case_date.get("status_code")
            message = case_date.get("message")
            test_data.append((account, password, status_code, message))
        return test_data
    if f:
        f.close()


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建Session对象

    def tearDown(self):
        if self.session:
            self.session.close()

    @parameterized.expand(build_data())
    def test01_login(self, account, password, status_code, message):
        response = self.login_api.login(self.session, account, password)
        self.assertEqual(status_code, response.status_code)
        # print(response.json())
        self.assertEqual(message, response.json().get("message"))
