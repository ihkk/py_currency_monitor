from wechat_bot import qywx_push, qywx_pic
from text_generator import gen_cur_msg
from fetch_price import get_price, get_jpy_img
from datetime import datetime
import hashlib
import base64
from PIL import Image
from io import BytesIO
# 判断时间
time_now = datetime.now()
current_hour = int(time_now.strftime("%H"))

# 企业微信机器人webhook TODO
webhook = ""
jpy_price, jpy_update = get_price("JPY")
eur_price, eur_update = get_price("EUR")


# 每天18点发送日元牌价图片
if current_hour != 18:
    img = get_jpy_img()
    # calculate md5 of the file
    img = Image.open(BytesIO(img))
    img = img.convert('RGB')
    img = img.save('img.jpg')
    # open img.jpg
    img = open('img.jpg', 'rb').read()
    md5 = hashlib.md5(img).hexdigest()
    # convert from bytes to base64
    img_base64 = base64.b64encode(img).decode('utf-8')
    # sent message
    qywx_pic(webhook, img_base64, md5)


# 只在白天提醒
if current_hour >= 8 or current_hour < 1:
    if float(jpy_price) > 5.05 and float(eur_price) > 800:
        text = f"JPY {jpy_price} EUR {eur_price}"
        qywx_push(webhook,text)
    else:
        # 日元牌价
        # 如果日元牌价低于0.51，就mention @all 否则只发送推送
        if float(jpy_price) < 5.05:
            text = gen_cur_msg("日元", jpy_price, jpy_update)
            mention = ["@all"]
            qywx_push(webhook,text,mention)
        else:
            text = f"JPY {jpy_price} @{jpy_update}"
            qywx_push(webhook,text)

        # 欧元牌价
        # 如果欧元牌价低于8，就mention @all 否则只发送推送
        if float(eur_price) < 800:
            text = gen_cur_msg("欧元", eur_price, eur_update)
            mention = ["@all"]
            qywx_push(webhook,text,mention)
        else:
            text = f"EUR {eur_price} @{eur_update}"
            qywx_push(webhook,text)
            
