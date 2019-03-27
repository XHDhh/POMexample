#coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.find_element = FindElement(driver)
    #获取邮箱元素
    def get_email_element(self):
        return self.find_element.get_element("user_email")
    def get_user_name(self):
        return self.find_element.get_element("user_name")
    def get_user_password(self):
        return self.find_element.get_element("password")
    def get_user_text(self):
        return self.find_element.get_element("code_text")
    def get_button_element(self):
        return self.find_element.get_element("register_button")
    def get_email_error_element(self):
        return self.find_element.get_element("user_email_error")
    def get_name_error_element(self):
        return self.find_element.get_element("user_name_error")
    def get_password_error_element(self):
        return self.find_element.get_element("password_error")
    def get_code_text_error_element(self):
        return self.find_element.get_element("code_text_error")