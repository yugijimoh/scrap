import re
import requests
import time
key="python"
url="https://yq.aliyun.com/search/articles/"
data=requests.get(url,params={"q":key}).text
pat1='<div class="_search-info">找到(.*?)条关于“<span>python</span>”信息</div>'
defaultpage=re.compile(pat1,re.S).findall(data)[0]
pages=int(defaultpage)//15+1
for i in range(0,pages):
    pg=i+1
    getdata={"q":key,"p":str(pg)}
    print("scaping page "+ str(pg))
    data=requests.get(url,params=getdata).text
    pat_article='<div class="media-body text-overflow">.*?<a href="(.*?)">'
    links=re.compile(pat_article,re.S).findall(data)
    baseurl="https://yq.aliyun.com"
    devurl="https://developer.aliyun.com"
    https://yq.aliyun.com/articles/765928
    pat_title='<title>(.*?)</title>'
    pat_cont='<div class="content-detail unsafe markdown-body">(.*?)<div class="copyright-outer-line">'
    for a in links:
        suburl=baseurl+a
        pagedata=requests.get(suburl).text
        try:
            title=re.compile(pat_title,re.S).findall(pagedata)[0]
            content=re.compile(pat_cont,re.S).findall(pagedata)[0]
        except Exception :
            suburl=devurl+a
            print("Error happen in page "+str(pg)+", title : "+title+"; try another url: "+suburl)
            try:
                pagedata=requests.get(suburl).text
                pat_cont2='<div class="content-detail unsafe markdown-body">(.*?)<div class="copyright-outer-line">'
                content=re.compile(pat_cont2,re.S).findall(pagedata)[0]
            except Exception as e:
                print("Failed to scape page "+str(pg)+", title : "+title+"; url: "+suburl+"; skip article")
                continue
        with open("pages\\"+str(i)+"_"+title+"_"+str(time.time())+".html","w",encoding="utf-8",errors="ignore") as fd:
            fd.write(title+"<br/><br/>"+content)
        fd.close()
print("scraping completed")