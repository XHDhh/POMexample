from selenium import webdriver
from base.find_element import FindElement
import time

class ActionMethod:
    def __init__(self):
        pass
    #打开浏览器
    def open_browser(self,browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()

    #输入地址
    def get_url(self,url):
        self.driver.get(url)

    #定位元素
    def get_element(self,key):
        find_element =FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    #输入元素
    def element_send_key(self,value,key):
        element = self.get_element(key)
        element.send_keys(value)

    #点击元素
    def click_element(self,key):
        self.get_element(key).click()

    #等待
    def sleep_time(self):
        time.sleep(3)

    #关闭浏览器
    def close_browser(self):
        self.driver.close()

    #获取title
    def get_title(self):
        return self.driver.title