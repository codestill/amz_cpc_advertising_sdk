# coding:utf-8
"""
Report 相关操作, 具体参数请参见 对应的json配置文件
"""

from . import MainBaseApi


class Report(MainBaseApi):
    """
    campaigns  info 
    """

    def campaigns(self, params=None):


        self.uri_path = '/v1/campaigns/reports'
        self.data = params
        self.method = 'get'
        return self.make_call()

    def adgroups(self, params=None):

        self.uri_path = '/v1/adgroups/reports'
        self.method = 'get'
        self.data = params
        return self.make_call()

    def keyword(self, params=None):

        self.uri_path = '/v1/keyword/reports'
        self.method = 'get'
        self.data = params
        return self.make_call()


class TypeReport(MainBaseApi):
    """
    按类型的广告报告
    """

    def get(self, report_id):
        """
        根据report获取信息
        """
        self.uri_path = '/v1/reports/{reportId}'.format(reportId=report_id)
        self.data = None
        self.method = 'get'
        return self.make_call()
    
    def create(self, report_type, params):

        """
        report type
        oneof:campaigns, adGroups, keywords,or productAds
        {“campaignType”: “sponsoredProducts”,“segment”:”query”,“reportDate”:”20150510”,“metrics”:”impressions,clicks”}
        """
        self.uri_path = '/v1/{type}/report'.format(type=report_type)
        self.method = 'post'
        self.data = params
        print self.uri_path
        return self.make_call()

    def download(self, loc_path):
        """
        下载
        """
        return self.public_call(loc_path)
 
