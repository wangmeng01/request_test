import logging
import os
import datetime

class User_Log:
    def __init__(self,log_type='debug'):

        if log_type == 'debug':
            self.logger=logging.getLogger('endlesscode')
            self.logger.setLevel(logging.DEBUG)
            #文件名
            bass_dir=os.path.dirname(os.path.abspath(__file__))
            log_dir=os.path.join(bass_dir,'logs')
            log_file='debug.'+datetime.datetime.now().strftime("%Y-%m-%d")+".log"
            log_name=log_dir+"\\"+log_file
            #文件输出日志
            self.file_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
            formatter=logging.Formatter('%(asctime)s,%(funcName)s,%(levelno)s:%(levelname)s,%(message)s')
            self.file_handle.setFormatter(formatter)
            self.logger.addHandler(self.file_handle)
    def get_log(self):
        return self.logger
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()
if __name__ == '__main__':
    user=User_Log('debug')
    user.logger.debug('aaaaaaaaaaaaa')
