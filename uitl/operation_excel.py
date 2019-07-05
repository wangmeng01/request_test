#coding:utf-8
import xlrd
from xlutils.copy import copy

class Operation_Excel():

    def __init__(self,filepath=None,sheet_id=None):
        if filepath == None and sheet_id == None:
            filepath=r'G:\接口实战\data_config\interface.xls'
            self.filepath=filepath
            self.sheet_id=0
        else:
            self.filepath=filepath
            self.sheet_id=sheet_id
        self.excel=self.get_excel(self.sheet_id)

    #打开excel获取sheet_id标签页的数据
    def get_excel(self,sheet_id):
        excel=xlrd.open_workbook(self.filepath)
        tables=excel.sheets()[sheet_id]
        return tables
    #获取excel中已存在数据的行数
    def get_lines(self):
        table_nrows=self.excel.nrows
        return table_nrows
    #获取excel中某个单元格中的内容
    def get_cell(self,row,col):
        data=self.excel.cell_value(row,col)
        return data

    #向excel中某个单元格写入内容
    def write_data(self,row,col,value):
        read_value=xlrd.open_workbook(self.filepath)
        read_data=copy(read_value)
        read_save=read_data.get_sheet(0)
        read_save.write(row,col,value)
        read_data.save(self.filepath)

    #获取某一列的数据内容
    def get_col_value(self,col=None):
        if col == None:
           cols=self.excel.col_values(0)
        else:
            cols=self.excel.col_values(col)
        return cols

    #根据对应的依赖id找到对应的行号
    def get_row_num(self,case_id):
        num=0
        cols_data=self.get_col_value()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num=num+1

    #根据行号找到该行的内容
    def get_row_value(self,row):
        tables=self.excel
        row_data=tables.row_values(row)
        return row_data

    #根据对应的case_id找到对应行的内容
    def get_row_data(self,case_id):
        row_num=self.get_row_num(case_id)
        row_data=self.get_row_value(row_num)
        return row_data
if __name__ == '__main__':
    op=Operation_Excel()
    list=op.get_row_data('5')
    print(list)
