# amz_cpc_advertising_sdk

python amazon cpc advertising api sdk

1. 修改 ad_account.py中的信息为你自己的开发者账号
2. 获取授权
 >1获取授权url
 >>from auth import BaseAuth <br>
 >>ba = BaseAuth()<br>
 >>print ba.get_grant_url()

 >2 获取code<br>
 >将上一步获取到的url在浏览器打开，输入卖家登陆信息，确认授权，取得code<br>
 
 >3获取 access_token 和refresh_token<br>
 >>print ba.get_refresh_token()
 
3.获取 profile
>from profiles import Profiles<br>
>profile = Profiles()<br>
>print profile.get_profiles()<br>
  
4. example， 使用sdk， 比如获取campaign
>from campaigns import Campaigns<br>
>profile_id = xxxxxx<br>
>access_token = 'xxxxxxxxxxxx'<br>
>camp = Campaigns(profile_id,access_token)<br>
>camp.list_extended()
