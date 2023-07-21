# generate message of currency price

def gen_cur_msg(cur,price,update_time):
    txt = f"💱汇率订阅提醒\n================\n每100{cur} {price} 人民币\n（现汇卖出价） \n\n数据来源：中国工商银行人民币即期外汇牌价\n\n发布时间：{update_time}\n\n"
    return txt