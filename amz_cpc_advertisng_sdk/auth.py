# coding:utf-8 -*-
import requests
from ad_account import client_id, redirect_uri, client_secret


class BaseAuth:
    """
    亚马逊advertisting api 授权管理
    1. 生成授权url
    2. 获取refresh_token
    3. 更新access_token
    """
    scope = 'cpc_advertising:campaign_management'
    response_type = 'code'
    host_grant = 'https://www.amazon.com/ap/oa'
    token_uri = 'https://api.amazon.com/auth/o2/token'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    def __init__(self):
        pass

    def get_grant_url(self):
        """
        获取授权页面
        """
        return '{host_grant}?client_id={client_id}&scope={scope}&response_type={response_type}&redirect_uri={redirect_uri}'.format(
            host_grant=self.host_grant,
            client_id=client_id,
            scope=self.scope,
            response_type=self.response_type,
            redirect_uri=redirect_uri)

    def get_refresh_token(self, code):
        """
        根据上一步授权获取的code,获取refreshtoken
        """
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret
        }

        ret = requests.post(self.token_uri, data, headers=self.header)

        print ret.json()

        info = ret.json()
        access_token, refresh_token = info['access_token'], info[
            'refresh_token']
        return access_token, refresh_token

    def new_access_token(self, refresh_token):
        """
        用refresh token 换取新的access_token
        """
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        }

        ret = requests.post(self.token_uri, data, headers=self.header)

        info = ret.json()

        access_token = info['access_token']

        return access_token


if __name__ == '__main__':

    ba = BaseAuth()
    print ba.get_grant_url()