#coding:utf-8
from data.get_data import Get_Data
from data.dependdent import DependdentData
from base.run_request import Run_Request
from uitl.comm_uitl import CommonUtil
from log.log import User_Log
from uitl.send_email import Send_Email
from config.config_T import Config_Try_Num
class Run_Main():
    def __init__(self):
        self.data=Get_Data()
        self.run_request=Run_Request()
        self.com_util = CommonUtil()
        self.send_email=Send_Email()
        self.user_log=User_Log()
        self.open_logging=self.user_log.get_log()

    def go_on_run(self):
        error_num=1
        passlist=[]
        faillist=[]
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run == True:
                while error_num <= Config_Try_Num:
                    url = self.data.get_url(i)
                    method = self.data.get_request_method(i)
                    data = self.data.read_data_for_json(i)
                    expect = self.data.get_expect_data(i)
                    depend_case = self.data.is_depend(i)
                    if depend_case != None:
                        self.depend_data = DependdentData(depend_case)
                        depend_response_data = self.depend_data.get_data_for_key(i)
                        depend_key = self.data.get_depend_field(i)
                        data[depend_key] = depend_response_data

                    res = self.run_request.run_type(method, url, data)
<<<<<<< 33ff303abff849283b3ec9ae931988254b2d372b
                    self.open_logging.info('<input> url:%s,请求方式:%s,参数:%s,预期:%s,result%s' % (url, method, data, expect, res))
=======
                    self.open_logging.debug('<input> url:%s,请求方式:%s,参数:%s,预期:%s,<result>%s' % (url, method, data, expect, res))
>>>>>>> add email
                    if self.com_util.is_contain(expect, res):
                        error_num = 1
                        # print('测试通过')
                        passlist.append(i)
                        self.data.write_result(i, 'pass')

                        break

                    else:
                        if error_num < Config_Try_Num:
                        #print(self.error_num)
                            error_num=error_num+1

                        else:
                            error_num = 1
                            faillist.append(i)
                            self.data.write_result(i, res)
                            break
        self.send_email.send_main(passlist,faillist)
if __name__ == '__main__':
    run=Run_Main()
    run.go_on_run()