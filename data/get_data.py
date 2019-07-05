#coding:utf-8
from uitl.operation_excel import Operation_Excel
from uitl.operation_json import OperationJson
from data import data_config
class Get_Data():
    def __init__(self):
        self.opera_excel=Operation_Excel()
        self.opera_json=OperationJson()
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    def get_is_run(self,row):
        col=data_config.get_is_run()
        run_model=self.opera_excel.get_cell(row,col)
        if run_model == 'yes':
            flag=True
        else:
            flag=False
        return flag
    def get_request_method(self,row):
        col=data_config.get_method()
        request_method=self.opera_excel.get_cell(row,col)
        return request_method

    def get_url(self,row):
        col=data_config.get_url()
        url=self.opera_excel.get_cell(row,col)
        return url
    #获取请求数据
    def get_request_data(self,row):
        col=data_config.get_data()
        data=self.opera_excel.get_cell(row,col)
        if data == '':
            return None
        return data
    #通过获取关键字拿到data数据

    #获取预期结果
    def get_expect_data(self,row):
        col=data_config.get_expect()
        expect=self.opera_excel.get_cell(row,col)
        if expect == '':
            return None
        return expect
    #写入实际结果
    def write_result(self,row,value):
        col=data_config.get_result()
        self.opera_excel.write_data(row,col,value)

    def get_depend_key(self,row):
        col=data_config.get_data_depend()
        depent_key=self.opera_excel.get_cell(row,col)
        if depent_key == '':
            return None
        else:
            return depent_key

    def is_depend(self,row):
        col=data_config.get_case_depend()
        depend_case_id=self.opera_excel.get_cell(row,col)
        if depend_case_id == '':
            return None
        else:
            return depend_case_id
    #获取数据依赖字段
    def get_depend_field(self,row):
        col=data_config.get_field_depend()
        data=self.opera_excel.get_cell(row,col)
        if data == '':
            return None
        else:
            return data
    def read_data_for_json(self,row):
        resquest_data=self.opera_json.get_data(self.get_request_data(row))
        return resquest_data

if __name__ == '__main__':
    data=Get_Data()
    res=data.get_case_lines()
    print(res)