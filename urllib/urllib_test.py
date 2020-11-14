import urllib.request as ureq
import random
import re
uapools= [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
]
def UA():
    opener=ureq.build_opener()
    thisua=random.choice(uapools)
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]
    ureq.install_opener(opener)
    print("当前UA是：{}",str(thisua))

#url = "https://nekocartplatium.xyz"
baseurl="https://www.qiushibaike.com/text/page/"
res=[]
for i in range(0,13):
    if i%3==0:
        UA()
    thisurl=baseurl+str(i)+"/"
    data=ureq.urlopen(baseurl).read().decode("utf-8","ignore")
    patt='<div class="content">.*?<span>.*?</span>.*?</div>'
    res=re.compile(patt,re.S).findall(data)

with open("baike.txt","w+", encoding="utf-8") as f1:
    for itm in res:
        f1.write(itm)
f1.close()