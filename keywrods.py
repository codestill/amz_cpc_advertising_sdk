# coding:utf-8
"""
keywords 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class Keywords(MainBaseApi):
    """
    Adgroups  info 
    """

    def create(self, params):
        """
        pass
        """

        self.uri_path = '/v1/keywords'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get(self, keyword_id):

        self.uri_path = '/v1/keywords/{keyword_id}'.format(
            keyword_id=keyword_id)
        self.method = 'get'
        return self.make_call()

    def get_extended(self, keyword_id):

        self.uri_path = '/v1/keywords/extended/{keyword_id}'.format(
            keyword_id=keyword_id)
        self.method = 'get'
        return self.make_call()

    def put(self, params):
        """
        更新信息
        """
        self.uri_path = '/v1/keywords'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def delete(self, adgroup_id):
        """
        删除group
        """
        self.uri_path = '/v1/keywords/{adgroup_id}'.format(
            adgroup_id=adgroup_id)
        self.method = 'delete'
        return self.make_call()

    def list(self, **params):
        """
        列出 adgroups
        """

        self.uri_path = '/v1/keywords'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def list_extended(self, params):
        """
        详细信息
        """
        self.uri_path = '/v1/keywords/extended'
        self.data = params
        self.method = 'get'
        return self.make_call()
