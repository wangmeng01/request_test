#coding:utf-8

class global_Var():
    #case_id
    Case_id=0
    Name=1
    Url=2
    Is_Run=3
    Method=4
    Cookie=5
    Case_Depend=6
    Data_Depend=7
    Field_Depend=8
    Data=9
    Expect=10
    Result=11

def get_case_id():
    return global_Var.Case_id

def get_name():
    return global_Var.Name
def get_url():
    return global_Var.Url
def get_is_run():
    return global_Var.Is_Run
def get_method():
    return global_Var.Method
def get_cookie():
    return global_Var.Cookie
def get_case_depend():
    return global_Var.Case_Depend
def get_data_depend():
    return global_Var.Data_Depend
def get_field_depend():
    return global_Var.Field_Depend
def get_data():
    return global_Var.Data
def get_expect():
    return global_Var.Expect
def get_result():
    return global_Var.Result