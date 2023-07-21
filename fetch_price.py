# fetch price from ICBC
import requests
import json


def get_price(cur):
    price_url = "https://papi.icbc.com.cn/exchanges/ns/getLatest"
    r = requests.get(price_url)
    price_data = json.loads(r.text)
    for i in price_data['data']:
        if i['currencyENName'] == cur:
            return i['foreignSell'], i['publishDate'][5:7]+"/"+i['publishDate'][8:10]+" "+i['publishTime'][0:5]
    return None


def get_jpy_img():
    week_url = "https://image.sinajs.cn/newchart/v5/forex/k/day/JPYCNY.gif"
    r = requests.get(week_url)
    return r.content
