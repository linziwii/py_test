'''
定义接口测试用例
使用unittest
'''

import requests
import unittest

from api.login import LoginAPI


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginAPI()  # 实例化接口类
        self.session = requests.Session()  # 创建Session对象

    def tearDown(self):
        if self.session:
            self.session.close()

    def test01_login_success(self):
        response = self.login_api.login(self.session, 'wujiaen', '1')
        self.assertEqual(200, response.status_code)
        # print(response.json())
        self.assertEqual("登录成功", response.json().get("message"))

    def test02_user_not_exist(self):
        response = self.login_api.login(self.session, 'wujiaen55', '1')
        self.assertEqual(200, response.status_code)
        # print(response.json())
        self.assertEqual("用户不存在，或用户名密码错误", response.json().get("message"))

    def test03_pwd_error(self):
        response = self.login_api.login(self.session, 'wujiaen', '11')
        self.assertEqual(200, response.status_code)
        # print(response.json())
        self.assertEqual("用户不存在，或用户名密码错误", response.json().get("message"))
