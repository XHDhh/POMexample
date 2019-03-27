#coding=utf-8
from selenium import webdriver
from business.register_business import  RegisterBusiness
from log.user_log import UserLog
import unittest
import time
import os
import HTMLTestRunner

logger = UserLog().get_log()

class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code_png = 'H:/PYwork/POMexample/test001.png'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register?goto=/course/explore')
        logger.info("this is Chrome")
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)


    def tearDown(self):
        time.sleep(3)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.path.dirname(os.getcwd())+'/report/'+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    def test_login_email_error(self):
        email_error = self.login.login_email_error('34','user111','111111',self.code_png)
        return self.assertFalse(email_error,"测试失败")
        #if email_error == True:
            #print("case失败")

    def test_login_username_error(self):
        pass

    def test_login_code_error(self):
        pass

    def test_login_success(self):
        self.login.user_base('12346@163.com','113125','444444',self.code_png)
        if self.login.register_success() == True:
            print('注册成功')

'''
def main():
    frist = FirstCase()
    frist.test_login_email_error()
    frist.test_login_username_error()
'''

if __name__ == '__main__':
    file_path = os.path.join("H:\\PYwork\\POMexample/report/firstreport.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_email_error'))
    #unittest.main()
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="first report",description=u"这是第一次测试",verbosity=2)
    runner.run(suite)
