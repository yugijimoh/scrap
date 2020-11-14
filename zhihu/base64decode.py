import urllib.request
import re
import ssl
import urllib.parse
from http import cookiejar
import base64
import json
import hmac
from hashlib import sha1
import time

#add to avoid ssl issue
ssl._create_default_https_context=ssl._create_unverified_context

#process cookie
print("processing cookie...")
cjar= cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

print("cookie processed. Signing in...")
url1="https://www.zhihu.com"
req0=urllib.request.Request(url1)
req0.add_header("User-Agent",'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0')
req0data=urllib.request.urlopen(req0).read().decode('utf-8','ignore')

#process catpcha
oauth="c3cef7c66a1843f8b3a9e6a1e3160e20"
code1="https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
req0=urllib.request.Request(code1)
req0.add_header("User-Agent",'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0')
req0.add_header("authorization",'oauth'+str(oauth))
req0data=urllib.request.urlopen(req0).read().decode("utf-8","ignore")
#why again??
req0=urllib.request.Request(code1,method="PUT")
req0.add_header("User-Agent",'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0')
req0.add_header("authorization",'oauth'+str(oauth))
req0data=urllib.request.urlopen(req0).read().decode("utf-8","ignore")
pat_code="img_base64'.'(.*?)'"
code_data=re.compile(pat_code,re.S).findall(req0data)
if (len(code_data)>0):
    code_data=code_data[0]
    code_img=base64.b64decode(code_data.replace("\\n",""))
    fh=open("./zhihucode.jpg","wb")
    fh.write(code_immg)
    fh.close()
else:
    code_data=""
    code_type=input("input code type: [1] reverse character, [2] direct input " )
    code_map={
        1:[22.796875,22],
        2:[42.796875,22],
        3:[63.796875,21],
        4:[84.796875,20],
        5:[107.796875,20],
        6:[129.796875,22],
        7:[150.796875,22]
    }
if(code_type=="1"):
    code_id=input("input the index of the reversed character: ")
    captcha={
        "img_size":[200,44],
        "input_points":[]
    }
    code_id=eval(code_id)
    for num in code_id:
        captcha['input_points'].append(code_map[num])
    code_value=json.dumps(captcha)
else:
    code_value=input("input the code: ")

codeposturl="https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
codepostdata=urllib.parse.urlencode({"input_text":code_value}).encode('utf-8')
req1=urllib.request.Request(codeposturl,codepostdata)
req1data=urllib.request.urlopen(req1).read().decode("utf-8","ignore")

#signature handling
def get_signature(grantType,clientId,source,timestamp):
    hm=hmac.new(b'')
    hm.update(str.encode(grantType))
    hm.update(str.encode(clientId))
    hm.update(str.encode(source))
    hm.update(str.encode(str(timestamp)))
    return str(hm.hexdigest())


