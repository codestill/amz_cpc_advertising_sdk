# amz_cpc_advertising_sdk

python amazon cpc advertising api sdk

1. 修改 ad_account.py中的信息为你自己的开发者账号
2. 获取授权
1）获取授权url
 >from auth import BaseAuth
 ba = BaseAuth()
 print ba.get_grant_url()
2) 获取code
将上一步获取到的url在浏览器打开，输入卖家登陆信息，确认授权，取得code
3）获取 access_token 和refresh_token
3.获取 profile
from profiles import Profiles
profile = Profiles()
print profile.get_profiles()
  
4. example， 使用sdk， 比如获取campaign
from campaigns import Campaigns
profile_id = xxxxxx
access_token = 'xxxxxxxxxxxx'
camp = Campaigns(profile_id,access_token)
camp.list_extended()
