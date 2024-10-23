import requests
import time

# 获取当前的13位时间戳（毫秒）
current_timestamp = int(time.time() * 1000)

# 将时间戳替换到URL中
url = f"https://mxsa.mxbc.net/api/v1/customer/signin?t={current_timestamp}&appId=d82be6bbc1da11eb9dd000163e122ecb&sign=FF9Ia7B2VOK6PMjzDb4stfpNJsUT9U4rnpT0oabz7sfsKLu1UhKs4mQMau6K4xoH2buDbRxZjiznhB3ZpCbboXTpEckCrr61GkSGVKfINb55J3UP9odyBb8r8jl3b9rlX2VT9OQe-dOBOjXPjKN2pclkAGOowyOCIvKfA1hjGeE7fs3SWrCyt7EbO_7vclyeGxQtHW578YBa4E-LikZmxwRkJtnZOgr8MRUv9EG8eF0rnrqZRGm_2Ro4E5SyCpZJcs23sycb8boQxQQdBeWbBrqlZ4e0Hen13GofhobR_0ea9RBIiOl85l6fwrAx4usIJUeqWcDZpPcc7ENgD6qIFQ%3D%3D"

headers = {
    "Host": "mxsa.mxbc.net",
    "Connection": "keep-alive",
    "charset": "utf-8",
    "x-ssos-cid": "1822966105392881665",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; MI 9 Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240301 MMWEBID/7437 MicroMessenger/8.0.48.2580(0x28003035) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/json",
    "access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ3eF8xODIyOTY2MTA1MzkyODgxNjY1IiwiaWF0IjoxNzI5MzQ0MTU4fQ.bor7ATcAnX0TFd9e9ESPlkpjv9OJEkuExCbuPguIqP892uh48X-TSbTMGRCfWFPRbC4hE4ICxH9Br-f2id6gfQ",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "version": "2.3.7",
    "Referer": "http"
}

res = requests.get(url, headers=headers)
print(res.text)
