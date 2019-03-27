#coding=utf-8
from page.register_page import RegisterPage
from util.get_code import GetCode

class RegisterHandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    #输入用户名
    def send_user_name(self,username):
        self.register_p.get_user_name().send_keys(username)
    #输入密码
    def send_user_password(self,password):
        self.register_p.get_user_password().send_keys(password)
    #输入验证码
    def send_user_text(self,code_png):
        get_code_text = GetCode(self.driver)
        #code = get_code_text.code_image(code_png)
        self.register_p.get_user_text().send_keys('code')
    #获取文字信息
    def get_user_text(self,info,user_info):
        #text_info = ''
        try:
            if info =='user_email_error':
                text_info = self.register_p.get_email_error_element().text
            elif info =='user_name_error':
                text_info = self.register_p.get_name_error_element().text
            elif info =='password_error':
                text_info = self.register_p.get_password_error_element().text
            else:
                text_info =self.register_p.get_code_text_error_element().text
        except:
            text_info = None
        return text_info
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
    #
    def get_register_button(self):
        return self.register_p.get_button_element().text