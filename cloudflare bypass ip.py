import requests
import re
import socket
from bs4 import BeautifulSoup
print ("""
##################################
#   Cüney Tanrısever             #
#   Cloudflare ip bypass tool    #
##################################""")
domain=input("domain: https // http // www ile başlamasın\nÖrnek: google.com gibi yazınız : ").replace("http://","").replace("https://","").replace("www.","")
def dnsdumper(domain):
    print ("Dns Dumper başladı")
    url = 'https://dnsdumpster.com'
    uag = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    get_token = requests.get(url,headers={'User-Agent':uag})
    token = re.findall("name=\"csrfmiddlewaretoken\" value=\"(.*?)\">",get_token.text)
    cookie=dict(get_token.cookies)
    cokietoken=cookie['csrftoken']
    veri={'csrfmiddlewaretoken':token,'targetip':domain,"user":"free"}
    cookies=dict(csrftoken=cokietoken)
    headers = {'User-Agent':uag,'Referer':url}
    post1 = requests.post(url, data=veri, cookies=cookies, headers=headers)
    ipler=re.findall("</td><td class=\"col-md-3\">(.*?)<br><span styl",post1.text)[0::2]
    if ipler==[]:
        print("dnsdumper başarısız")
    else:
        print("Dns dumperden gelen ipler")
        for i in ipler:
            print("ip = ",i)
        print("----------------------------------------------------")
def kabakuvvet(domain):
    print("Brute Başladı")
    sublar=["www","mail","ftp","localhost","webmail","smtp","pop","ns1","webdisk","ns2","cpanel","whm","autodiscover","autoconfig","m","imap","test","ns","blog","pop3","dev","www2","admin","forum","news","vpn","ns3","mail2","new","mysql","old","lists","support","mobile","mx","static","docs","beta","shop","sql","secure","demo","cp","calendar","wiki","web","media","email","images","img","www1","intranet","portal","video","sip","dns2","api","cdn","stats","dns1","ns4","www3","dns","search","staging","server","mx1","chat","wap","my","svn","mail1","sites","proxy","ads","host","crm","cms","backup","mx2","lyncdiscover","info","apps","download","remote","db","forums","store","relay","files","newsletter","app","live","owa","en","start","sms","office","exchange","ipv4"]
    for i in sublar:
        domains=i+"."+domain
        try:
            ipbul= socket.gethostbyname(domains) 
            print("ip:",ipbul,"bulunan domain = ",domains)
        except:
            pass
    print("----------------------------------------------------")
def cloud(domain):
    print ("crimeflare deneniyor")
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)' }
    rq=requests.session()
    rq.headers.update(headers)
    url="http://www.crimeflare.org:82/cgi-bin/cfsearch.cgi"
    post="cfS=%s"%(domain)
    git=rq.post(url,data=post)
    kaynak=str(git.content)
    kaynak.encode("utf-8")
    kontrol=["search error","No working nameservers are registered","No direct-connect IP address was found for this domain","these are not CloudFlare-user nameservers"]
    bulundu=False
    for  i in kontrol:
        if i in kaynak:
            print (i)
        else:
            try:
                ip = re.search("\d*\.\d*\.\d*\.\d*", kaynak).group()
                if ip !="":
                    print ("site = {}".format(domain))
                    print ("Gercek ip = {}".format(ip))
                    bulundu=True
                    break
            except AttributeError:
                continue
    if bulundu==False:
        print ("Bulunamadı")
            
dnsdumper(domain)
kabakuvvet(domain)
cloud(domain)
