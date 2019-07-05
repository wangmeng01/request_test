#coding:utf-8
import json
class OperationJson():
    def __init__(self,filepath=None):
        if filepath == None:
            self.filepath=r'G:\study\data_config\login.json'
        else:
            self.filepath=filepath
        self.data=self.read_json()
    def read_json(self):
        with open(self.filepath) as fp:
            data=json.load(fp)
            return data

    def get_data(self,key):
        return self.data[key]

    def write_data(self,data):
        with open('../data_config/cookie.json','w') as fp:
            fp.write(data)