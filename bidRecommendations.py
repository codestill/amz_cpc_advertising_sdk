# coding:utf-8
"""
bidRecommendations 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class BidRecommendation(MainBaseApi):
    """
    bidRecommendations  info 
    """

    def adgroup(self, adgroup_id):
        """
        Bid recommendation for AD group in Manual Targeted Campaign is not supported
        """

        self.uri_path = '/v1/adGroups/{adGroupId}/bidRecommendations'.format(adGroupId=adgroup_id)
        self.method = 'get'
        return self.make_call()

    def keyword(self, keyword_id):
        """
         Bid recommendation for keyword in auto Targeted Campaign is not supported
        """
        self.uri_path = '/v1/keywords/{keywordId}/bidRecommendations'.format(keywordId=keyword_id)
        self.method = 'get'
        return self.make_call()

    def keyword_list(self, params=None):

        self.uri_path = '/v1/keywords/bidRecommendations'
        self.method = 'post'
        self.data = params
        return self.make_call()


