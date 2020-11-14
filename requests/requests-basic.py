'''
request method: GET, POST, PUT
parameters: params headers, proxies, cookies, data
text: response
content
encoding
cookies
url
status code
'''
import requests
import re
hdr={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
#px={"http":"http://127.0.0.1:8866"}
#coki={"":""}
#rst=requests.get("https://hsbc.com.cn",headers=hdr)
#title=re.compile("<title>(.*?)</title>",re.S).findall(rst.text)
#print(title)
params={"q":"女巨人"}
rst2=requests.get("https://cn.bing.com/search",params=params)
print(f"encoding: {rst2.encoding}; \n url: {rst2.url}; \n cookies: {requests.utils.dict_from_cookiejar(rst2.cookies)}")
dt={"name":"adsf","pass":"jjjj"}
res=requests.post("https://www.iqianyue.com/mypost",data=dt)
print(res.text)