import requests

headers = {
    'Host': 'mk.donixtech.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '2',
    'Accept': 'application/json, text/plain, */*',
    'X-Token': 't51ip8c3h6cima038lgifhd8n3',
    'Token-Only': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; MI 9 Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/7437 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://mk.donixtech.com',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mk.donixtech.com/data-html/store/1.1.0/card/?app_code=JiuHongShengHuoCSCTD&card_id=pQuqy6ppNV3tRor5UKLRTzuGm68U&encrypt_code=7rr5R0Y%2BMnTbw4bDGR2FWO4aMwYAJ1TMKptn5DcOLi4%3D&openid=oQuqy6maJH_9TbO2Wvk83oqsrY_w',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

json_data = {}

response = requests.post(
    'https://mk.donixtech.com/card/app/index.php?_act_=member-card/sign-day&rsp=json&vv_run_in=0423',
    headers=headers,
    json=json_data,
)

print(response.text)