# --*utf-8*--
import unittest
from PageObject.common.browser import browser
from PageObject.actions.login_action import LoginAction
from PageObject.common.base_page import BasePage
from PageObject.common.config_utils import conf
from PageObject.element_infos.main.main_page import MainPage
from PageObject.common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):
    def setUp(self):
        '''如果遇到需要单独写的东西可以在运行代码中的setup里面 刷新操作'''
        '''调用父类的setUp'''
        super().setUp()
        print('helllo')

    # def tearDown(self):
    #     self.base_page.close_tab()

    '''登录成功'''
    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        mainpage=login_action.login_success(conf.zengtao_username,conf.default_password)
        actual_result=mainpage.get_usrname()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    '''登录失败'''
    def test_login_fail(self):
        login_action=LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail('sss','213123')
        print('actual_result%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail用例执行失败')
if __name__=="__main__":
    unittest.main()