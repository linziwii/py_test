'''
被测系统的接口封装
登陆：https://pangu.ucgsoft.cn/pangu/api/organization/user
'''


class LoginAPI():
    def __init__(self):
        self.login_url = 'https://pangu.ucgsoft.cn/pangu/api/organization/user'

    def login(self, session, account, password):
        login_data = {
            "account": account,
            "password": password
        }
        return session.post(url=self.login_url, json=login_data)

