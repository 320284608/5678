import requests
import time

# 获取当前的10位时间戳
current_timestamp = int(time.time())

url = "https://mapi.xiaotucc.com/we/user/lottery/take"
headers = {
    "Host": "mapi.xiaotucc.com",
    "Connection": "keep-alive",
    "charset": "utf-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; MI 9 Build/UKQ1.231003.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260093 MMWEBSDK/20240501 MMWEBID/7437 MicroMessenger/8.0.50.2701(0x2800325A) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Referer": "http"
}

# 替换timestamp为当前时间戳
#data = f"uid=3673043&timestamp={current_timestamp}&token=8B9C6C0FBBFD98386482C5F9C1948103971EC622"
data = """uid=3673043&timestamp=1725671456&token=8B9C6C0FBBFD98386482C5F9C1948103971EC622"""
res = requests.post(url, headers=headers, data=data)
print(res.text)
