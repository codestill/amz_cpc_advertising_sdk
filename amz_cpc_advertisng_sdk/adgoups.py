# coding:utf-8
"""
adgroups 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class Adgroups(MainBaseApi):
    """
    Adgroups  info 
    """

    def create(self, params):
        """
        # data = json.dumps([{
        "name": "The name of the ad group",
        "campaignId": "164121332960233",
        "defaultBid": 0.5,
        "state": "enabled"
        }
        ])
        """

        self.uri_path = '/v1/adGroups'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get(self, adgroup_id):

        self.uri_path = '/v1/adGroups/{adgroup_id}'.format(
            adgroup_id=adgroup_id)
        self.method = 'get'
        return self.make_call()

    def put(self, params):
        """
        更新信息
        """
        self.uri_path = '/v1/adGroups'
        self.data = params
        self.method = 'put'
        return self.make_call()

    def delete(self, adgroup_id):
        """
        删除group
        """
        self.uri_path = '/v1/adGroups/{adgroup_id}'.format(
            adgroup_id=adgroup_id)
        self.method = 'delete'
        return self.make_call()

    def list(self, **params):
        """
        列出 adgroups
        """

        self.uri_path = '/v1/adGroups'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def list_extended(self, params):
        """
        详细信息
        """
        self.uri_path = '/v1/adGroups/extended'
        self.data = params
        self.method = 'get'
        return self.make_call()
