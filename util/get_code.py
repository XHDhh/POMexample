#coding = utf-8
import pytesseract
import time
from PIL import Image
class GetCode():
    def __init__(self,driver):
        self.driver = driver
    # 获取图片
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id("getcode_num")
        #print(code_element.location)
        left = code_element.location['x']
        top = code_element.location['y']
        #print(code_element.size)
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片获取验证码
    def code_image(self,file_name):
        self.get_code_image(file_name)
        image = Image.open(file_name)
        text = pytesseract.image_to_string(image)
        if text == '':
            text = 'ERR'
        time.sleep(2)
        return text