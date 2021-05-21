#coding:utf-8
import os
import re
import time
import sys
import requests
os.system('cls' if os.name == 'nt' else 'clear')
print """
##################################
#        Cüneyt TANRISEVER       #
#        cloud ip bypass         #
##################################"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
rq=requests.session()
rq.headers.update(headers)

url="http://www.crimeflare.org:82/cgi-bin/cfsearch.cgi"
site=raw_input("site urlsini giriniz basinda http / https olmasin.\n google.com seklinde giriniz. = ")
pos="cfS=%s"%(site)

res=rq.post(url,data=pos)
rm=res.content
print rm 
try:
    kontrol="search error"
    if kontrol in rm:
        print "site = %s\n" %(site)
        print "Gercek ip si bulunamadi.  :("
        time.sleep(7)
        sys.exit
 
    kontrol1="No working nameservers are registered"
    if kontrol1 in rm:
        print "site = %s\n" %(site)
        print "Gercek ip si bulunamadi.  :("
        time.sleep(7)
        sys.exit()
    kontrol2="No direct-connect IP"
    if kontrol2 in rm:
        print "site = %s\n" %(site)
        print "Gercek ip si bulunamadi.  :("
        time.sleep(7)
        sys.exit
    

    ip = re.search("\d*\.\d*\.\d*\.\d*", rm).group()
    if ip !="":
        print "site = %s" %(site)
        print "Gercek ip = %s" %(ip)
        time.sleep(7)
except:
    pass
