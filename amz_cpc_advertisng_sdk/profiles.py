# coding:utf-8
"""
Profiles 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import BaseApi


class Profiles(BaseApi):
    """
    profiels info 
    """
    def register(self,**params):

        self.uri_path = '/v1/profiles/register'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def get_profiles(self):

        self.uri_path = '/v1/profiles'
        self.method ='get'
        return self.make_call()