import re
import requests

key="python"
area="030200"
param={
    "kw":key,
    "jl":"763",
    "kt":"3"
}
target_url="https://sou.zhaopin.com/?"
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

data=requests.get(target_url+"1.html",headers=hd,params=param)
info=bytes(data.text,data.encoding).decode("utf8","ignore")
print(info)
pat="共(.*?)条职位"
num=re.compile(pat,re.S).findall(info)[0]
print(num)
