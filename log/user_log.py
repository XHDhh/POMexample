#coding = UTF-8
import logging
import os
import datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #控制台输出日志
        #consle = logging.StreamHandler()
        #logger.addHandler(consle)

        #以当前时间命名日志文件
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"\\"+log_file

        #文件输出日志
        file_handle1 = logging.FileHandler(log_name,"a",encoding='utf-8')
        #设置等级
        file_handle1.setLevel(logging.INFO)
        #文件格式
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(lineno)d: %(levelname)s ---->%(message)s')
        file_handle1.setFormatter(formatter)

        self.logger.addHandler(file_handle1)

        #self.logger.debug("test1234")
        file_handle1.close()

        streamhandel = logging.StreamHandler()
        streamhandel.setLevel(logging.DEBUG)
        self.logger.addHandler(streamhandel)

        #consle.close()
        #logger.removeHandler(consle)
    def get_log(self):
        return self.logger