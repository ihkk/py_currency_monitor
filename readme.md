# 汇率检测推送脚本
将汇率信息推送到企业微信群。

## 使用方法
将本脚本放到crontab中定期执行。

## 脚本配置
1. 打开`update_cur.py`，填写企业微信群机器人hook地址。
2. `get_price('Currency')`函数用于获取实时购汇牌价。

## 使用效果
![preview](rdme_img/preview.png)

