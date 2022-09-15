import requests
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

    #return None #for debug

    IP = [] #this contains ip:port list through scrape data

    proxy_args = {
        'all': 'all',
        'http': 'http',
        'http-only': 'http',
        'https': 'https',
        'socks': 'socks',
        'socks4': 'socks4',
        'socks5': 'socks5',
    }

    security_args = {
        'all': 'all',
        'low': 'Transparent',
        'average': 'Anonymous',
        'high': 'Elite',
    }

    host = 'https://hidester.com/proxydata/php/data.php'

    #temp
    headers = {
        #'Host': 'hidemy.name',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Referer': 'https://hidester.com/proxylist/',
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'Connection': 'keep-alive',
        #'Cookie': '__cfduid=d6c29c886819d92283f66b1b2a69528a71606222113',
        #'Upgrade-Insecure-Requests': '1'
    }

    params = {
        'mykey':'data',
        'offset':0,
        'limit':1645,
        'orderBy':'latest_check',
        'sortOrder':'DESC',
        'type':'socks5',  #type not affecting in output
        'anonymity':'undefined', 
        'ping':'undefined',
        'gproxy':2,
    }

    if check_internet:
        response = requests.get(host,params=params,headers=headers)
        if response.status_code==200:
            data = response.json()
            for ip_scrap in data:
                
                if proxy_type == 'http' or proxy_type == 'socks':
                    if proxy_type in ip_scrap['type']:
                        if security_args[security_type] == 'all':
                            IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))
                        elif security_args[security_type] == ip_scrap['anonymity']:
                            IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))

                elif proxy_type != 'all':
                    #print(ip_scrap)
                    if proxy_args[proxy_type] == ip_scrap['type']:
                        if security_args[security_type] == 'all':
                            IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))
                        elif security_args[security_type] == ip_scrap['anonymity']:
                            IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))
                else:
                    if security_args[security_type] == 'all':
                        IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))
                    elif security_args[security_type] == ip_scrap['anonymity']:
                        #print(ip_scrap)
                        IP.append(ip_scrap['IP']+':'+str(ip_scrap['PORT']))

    

    return IP
