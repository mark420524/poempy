# -*- coding: utf8 -*-
from lxml import etree
from bs4 import BeautifulSoup
import requests
import random
import time
import io
headers = {
    #':authority':'www.gushiwen.org',
    #':method':'GET',
    #':path':'/gushi/tangshi.aspx',
    #':scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cache-control':'max-age=0',
    'cookie':'sec_tc=AQAAAPnRtw9rXgoAAcIXHmfJdTMAeJTb; Hm_lvt_04660099568f561a75456483228a9516=1557383565; Hm_lpvt_04660099568f561a75456483228a9516=1557383578',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}
file_name="allurl.txt"
poem_name="poemall.txt"


def grab_data(downurl):
    pass
def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

def get_proxies(): #随机IP
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url, headers=headers)
    proxies = get_random_ip(ip_list)
    return proxies
def main_down():
    url='https://www.gushiwen.org/gushi/tangshi.aspx'
    res = requests.get(url=url, headers=headers, proxies=get_proxies())
    res.encoding = 'utf-8'
    selector = etree.HTML(res.text)
    xpath_reg = '//div[@class="typecont"]//@href'
    results = selector.xpath(xpath_reg)
    return results
def get_poemUrl():
    results = main_down()
    str_convert = '\n'.join(results)
    with open(file_name, 'wb') as fp:
        fp.write(str_convert)
def read_url():
    poemUrl = []
    with open(file_name ) as file:
    	for line in file:
    		poemUrl.append(line.strip())
    return poemUrl
def down_content(url):
    res = requests.get(url=url, headers=headers )
    res.encoding = 'utf-8'
    divid='contson'+get_poemid(url)
    selector = etree.HTML(res.text)
    xpath_reg = '//div[@id="'+divid+'"]//text()'
    results = selector.xpath(xpath_reg)
    conent = ''.join(results)
    xpath_reg = '//h1//text()'
    results = selector.xpath(xpath_reg)
    name = results[0]
    xpath_reg = '//p[@class="source"]//text()'
    results = selector.xpath(xpath_reg)
    author= results[0] +results[1]+results[2]
    poem={}
    poem['name']=name.strip()
    poem['author']=author.strip()
    poem['conent']=conent.strip()
    return poem
def get_poemid(url):
    ids = url.split('shiwenv_')
    poemid=ids[1]
    return poemid[:-5]
def down_and_save(url):
    with io.open( poem_name ,"w",encoding="utf-8" ) as files:
        for i in url:
            print i
    	    content=down_content(i)
            files.write("%s %s %s \n" % (content['name'],content['author'],content['conent']))
    	    #休息一下
    	    time.sleep(5)
    return "ok"
if __name__ == '__main__':
    url=read_url()
    print down_and_save(url)
    