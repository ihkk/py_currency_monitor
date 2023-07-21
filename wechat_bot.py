# a interface to push message via wechat bot
import requests
import json

def qywx_push(webhook,text,mention_list=[]):
    url = webhook
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            "content": text,
            "mentioned_list": mention_list
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.text


def qywx_pic(webhook, pic, md5):
    url = webhook
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "image",
        "image": {
            "base64": pic,
            "md5": md5
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.text