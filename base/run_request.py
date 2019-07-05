#coding:utf-8
import requests
import json
class Run_Request():

    def post_type(self,url,data,header):
        res=None
        if header!=None:
            res=requests.post(url=url,data=data,header=header)
        else:
            res=requests.post(url=url,data=data)
        return res.json()
    def get_type(self,url,data=None,header=None):
        res=None
        if header !=None:
            res=requests.get(url=url,data=data,header=header,verify=False)
        else:
            res=requests.get(url=url,data=data,verify=False)
        return res

    def run_type(self,method,url,data=None,header=None):
        res=None
        if method == 'post':
            res=self.post_type(url,data,header)
        else:
            res=self.get_type(url,data,header)
        return json.dumps(res,ensure_ascii=False)
