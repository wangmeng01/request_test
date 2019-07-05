#coding:utf-8
from uitl.operation_excel import Operation_Excel
from base.run_request import Run_Request
from data.get_data import Get_Data
from jsonpath_rw import jsonpath,parse
import json
class DependdentData():
    def __init__(self,case_id):
        self.case_id=case_id
        self.opera_excel=Operation_Excel()
        self.data=Get_Data()

    def get_case_line_data(self):
        rows_data=self.opera_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependdent(self):
        run_method=Run_Request()
        row_num=self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.read_data_for_json(row_num)
        # header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_url(row_num)
        res = run_method.run_type(method, url, request_data)
        return json.loads(res)

    def get_data_for_key(self,row):
        depend_data=self.data.get_depend_key(row)
        response_data=self.run_dependdent()
        json_exe=parse(depend_data)
        madle=json_exe.find(response_data)
        return [math.value for  math in  madle]
