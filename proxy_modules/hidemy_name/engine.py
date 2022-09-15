import requests
from bs4 import BeautifulSoup as BS
from core.compatible import check_internet

#completed

def start(proxy_type, security_type, country):
    """
    takes all default args in start 

    Args: 
        mentioned in default config(not required)

    Return:
        array of tuple [('proxy_type', 'proxy')]

    """

    return None #for debug

    IP = [] #this contains ip:port list through scrape data

    proxy_args = {
        'all': '',
        'http': 'hs',
        'http-only': 'h',
        'https': 's',
        'socks': 45,
        'socks4': 4,
        'socks5': 5,
    }

    security_args = {
        'all': '',
        'low': 12,
        'average': 3,
        'high':4
    }

    #temp
    headers = {
        #'Host': 'hidemy.name',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'Connection': 'keep-alive',
        #'Cookie': '__cfduid=d6c29c886819d92283f66b1b2a69528a71606222113',
        #'Upgrade-Insecure-Requests': '1'
    }



    host = 'https://hidemy.name/en/proxy-list/'
    #print(host)

    params = {
        'type':proxy_args[proxy_type],      #for socks5
        'anon':security_args[security_type],      #for elite security
    }
    
    if proxy_type == 'all':
        params.pop('type')

    if security_type == 'all':
        params.pop('anon')

    if country!='all':
        params['country'] = country

    while True:
        if check_internet:
            response = requests.get(host,params=params,headers=headers)
            if response.status_code==200:
                data = BS(response.text,'lxml')
                ip_scrap = data.tbody.find_all(['td'])
                nxt_button = data.find('li',class_="next_array")

                ln=len(ip_scrap)
                skip=0

                while skip<ln:
                    IP.append(ip_scrap[skip].text+':'+ip_scrap[skip+1].text)
                    skip+=7

                if nxt_button == None:
                    break

                if 'start' in params.keys():
                    params['start']+=64
                else:
                    params['start']=64
    #print('proxy downloaded from HIDEmyname.')

    return IP