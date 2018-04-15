# coding:utf-8
"""
campaigns 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class Campaigns(MainBaseApi):
    """
    campaigns  info 
    """

    def create(self, params):
        """
        data = json.dumps([
            {
            "name": "Hello World Campaign",
            "state": "enabled",
            "startDate": "20290101",
            "campaignType": "sponsoredProducts",
            "targetingType": "auto",
            "dailyBudget": 1.00
        }
        ])
        """

        self.uri_path = '/v1/campaigns/'
        self.data = params
        self.method = 'post'
        return self.make_call()

    def get_campaign(self, campaign_id):

        self.uri_path = '/v1/campaigns/{campaign_id}'.format(
            campaign_id=campaign_id)
        self.method = 'get'
        return self.make_call()

    def get_extended_campaign(self, campaign_id):

        self.uri_path = '/v1/campaigns/extended/{campaign_id}'.format(
            campaign_id=campaign_id)
        self.method = 'get'
        return self.make_call()

    def list(self, params=None):

        self.uri_path = '/v1/campaigns'
        self.method = 'get'
        self.data = params
        return self.make_call()

    def list_extended(self, params=None):

        self.uri_path = '/v1/campaigns/extended'
        self.method = 'get'
        self.data = params
        return self.make_call()


