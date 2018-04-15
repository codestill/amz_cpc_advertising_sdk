# coding:utf-8
"""
Suggested 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class SuggestedKeyword(MainBaseApi):
    """
    SuggestedKeyword  info 
    """

    def adgroup(self, adgroup_id):
        """
        """

        self.uri_path = '/v1/adGroups/{adGroupId}/suggested/keywords'.format(adGroupId=adgroup_id)
        self.method = 'get'
        return self.make_call()

    def adgroup_extended(self, adgroup_id):
        """
        Getting keyword recommendations for AD Group in Auto Targeted Campaign is not supported
        """

        self.uri_path = '/v1/adGroups/{adGroupId}/suggested/keywords/extended'.format(adGroupId=adgroup_id)
        self.method = 'get'
        return self.make_call()

    def asin(self, asin):
        """
        """
        self.uri_path = '/v1/asins/{asin}/suggested/keywords'.format(asin=asin)
        self.method = 'get'
        return self.make_call()

    def asin_list(self, params=None):

        self.uri_path = '/v1/asins/suggested/keywords'
        self.method = 'post'
        self.data = params
        return self.make_call()


