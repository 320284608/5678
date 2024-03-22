import requests
from datetime import datetime

current_timestamp = int(datetime.timestamp(datetime.now()))

headers = {
    'Host': 'm.pailifan.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '486',
    'charset': 'utf-8',
    'b': '2617',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; 2201122C Build/UKQ1.231003.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/7437 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    # 'Accept-Encoding': 'gzip,compress,br,deflate',
    'deviceorientation': 'portrait',
    'version': '8.0.47',
    'platform': 'android',
    'token': 'It/opdR/CWIuBQQdkZY7jz+NYYgSQ6smSHeeRfskyLdwHI+fWLs6G6xA1cPyVKOOoG1KGeUc5L5kXV4W3OVUB/T3Q7Z77y5MulIUNNtgDuY5OR9MgcXMcsGEakPlBCxZv98Q0Uwb5uOJPhIXNiZ5B7EhT0rV26R+ihXW+0OSEe+RA9wnYhtZ/PNbjYWt1BAJY+IDx4aliTYIWKZLvFKUxFya2nO1S6GEdeWlYNKxvdKj9/kGuLmueG5Y2VQiPaWd',
    'system': 'Android 14',
    't': str(current_timestamp),
    'size': '393,835',
    'model': 'MI 9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'brand': 'Xiaomi',
    'Referer': 'https://servicewechat.com/wx2e7a6973da6a1b54/1305/page-frame.html',
}

json_data = {
    'encode': 'euGx2i8YLa83gy0i5p+3p2UtYdAMhHyWUnZ/zQqnqrnSTjgts5e5dO37PnBRRN/7NN1IbzsKyAAnDaTIvZG/KJAzHw46DEYgVDzEe1vICcJsAMU8P7PypqFavL7Y1SOUkbNm/wGDde8rHGR5nA4XEu3Ya30R+SYZ/mJcgfQbLxCP3f3T2q8NYRqKRR3PchoyJbFGejMaimw0VKkcf2K+5LcuKKn+qWJuVMTeaPiuqWT4DPC0pLziBxncV5TAbIRl+A36PTE0Dd6BC+dUKwfmzoJ/azc71OJudLV2hO8J7nGLoDRsLow89qJcQynDCmCFyU4v0yyKx/duSGvzDY/yPehvjmHVqVR80L6eSm95Dytg/AA5MGoSZO9O54aC3xEsx0giZd5u5Ks38it52ub4Oz9qnkt9ix3zNnJTrNO829oTT0l6jE0ifuhjpbv1zrpo',
    't': str(current_timestamp),
    'bd': 2617,
}

response = requests.post('https://m.pailifan.com/xcx/u/signinlog', headers=headers, json=json_data)
print(response.text)
