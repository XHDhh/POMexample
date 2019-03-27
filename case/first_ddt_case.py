#coding = utf-8
import ddt
import unittest
import time
import os
import HTMLTestRunner
from selenium import webdriver
from business.register_business import  RegisterBusiness
from util.excel_util import ExcelUtil
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.code_png = 'H:/PYwork/POMexample/test001.png'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register?goto=/course/explore')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.dirname(os.getcwd()) + '/report/' + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['123','user1234','12345678','code','register_email-error','请输入有效的电子邮件地址'],
        ['@qq.com', 'user1234', '12345678', 'code', 'register_email-error', '请输入有效的电子邮件地址'],
        ['4567@qq.com', 'user1234', '12345678', 'code', 'register_email-error', '请输入有效的电子邮件地址'],
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText = data
        email_error = self.login.register_function(email,username,password,code,assertCode,assertText)
        self.assertFalse(email_error,"测试失败")

if __name__ == '__main__':
    file_path = os.path.join("H:\\PYwork\\POMexample/report/firstreport2.html")
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="second report", description=u"这是第二次测试", verbosity=2)
    runner.run(suite)
