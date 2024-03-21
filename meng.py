import requests
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

headers = {
    'Host': 'mp-isv.youzanyun.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '192',
    'isv-token': '33c45ffd-1fb9-470b-bda0-8c61bcb91ed3',
    'charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; 2201122C Build/UKQ1.231003.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/7437 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'encryptionkey': 'YZ1219760574223540224YZrkhSqbjc',
    # 'Accept-Encoding': 'gzip,compress,br,deflate',
    'isv': 'mengniuxitongdatong.isv.youzan.com',
    'accept': 'application/json',
    'Referer': 'https://servicewechat.com/wx1342c59a70c7a94f/248/page-frame.html',
}

json_data = {
    'mobile': '18124096181',
    'storeId': 146881102,
    'actionName': '营养值赚取',
    'time': current_time,
    'proteinNumber': 5,
    'openId': 'uxEpsnqf1147302780348706816',
    'totalId': 252,
    'brand': 'GLOBAL',
}

response = requests.post('https://mp-isv.youzanyun.com/activity/add_sign_in_customer', headers=headers, json=json_data)
print(response.text)
