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
    #print("当前UA是：{0}",str(thisua))

res=[]
cid="6588784454226395333"
for i in range(0,10):
    url="https://video.coral.qq.com/varticle/4233073658/comment/v2?callback=_varticle4233073658commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(cid)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=1596346211567"
    print("Scaping Page {0}".format(str(i)))
    if i%3==0:
        UA()
    data=ureq.urlopen(url).read().decode("utf-8","ignore")
    patt='"content":"(.*?)"'
    res.append(re.compile(patt,re.S).findall(data))
    patt2='"last":"(.*?)"'
    cid=re.compile(patt2,re.S).findall(data)[0]
with open("qqvideocomm.txt","w+",encoding="utf8") as f1:
    for itm in res:
        for i in itm:
            f1.write(i)
            f1.write("\n---------\n")
        f1.write("\n=========================\n")
f1.close()