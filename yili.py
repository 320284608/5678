import requests

headers = {
    'Host': 'msmarket.msx.digitalyili.com',
    'Connection': 'keep-alive',
    # 'Content-Length': '2',
    'charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 14; MI 9 Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/7437 MicroMessenger/8.0.47.2560(0x28002F30) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'access-token': 'V9j64pihB4Vkmc3hTFid1dgSWlLTux+5lpRq3QIRfTmTEZ0vF/UerbxkEHCPmnHWuTADZd90XoRw3JCfrSSGmMYSxYRD8nE+6ixQK8dlPKU=',
    # 'Accept-Encoding': 'gzip,compress,br,deflate',
    'tenant-id': '1559474730809618433',
    'scene': '1005',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx06af0ef532292cd3/383/page-frame.html',
}

json_data = {}

response = requests.post('https://msmarket.msx.digitalyili.com/gateway/api/member/daily/sign', headers=headers, json=json_data)


print(response.text)
