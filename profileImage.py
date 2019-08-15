import requests

# 微信在 Android/iPhone 下的 User Agent
headers = {
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN'
}

cookies = {
    
}

url = 'https://mp.weixin.qq.com/s/JiXnE-fKPeJG10CK1B6zFw'

r = requests.post(url=url, headers=headers)
print(r)

html = r.text
print(html)