import requests
from bs4 import BeautifulSoup as BS
# from core.compatible import check_internet

#first get token
#less priority

def start(proxy_type, security_type, country):
    """
    takes all default args in start 

    Args: 
        mentioned in default config(not required)

    Return:
        array of tuple [('proxy_type', 'proxy')]

    """

    #return None #for debug

    # token, cookies = token_cookie()
    # host = 'https://www.proxyscan.io'
    host = "https://www.proxyscan.io/home/filterresult"

    proxy = []  #this is going to return as mentioned in function spec
    IP = [] #this contains ip:port list through scrape data


    proxy_args = {
        'all': 'all',
        'http': ['HTTP', 'HTTPS'],
        'http-only': 'HTTP',
        'https': 'https',
        'socks': ['SOCKS4', 'SOCKS5'],
        'socks4': 'SOCKS4',
        'socks5': 'SOCKS5',
    }

    security_args = {
        'all': 'all',
        'low': 'Transparent',
        'average': 'Anonymous',
        'high': 'Elite'
    }


    headers = {
        'Host': 'www.proxyscan.io',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
        # 'Accept': '*/*',
        # 'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': '132',
        'Origin': 'https://www.proxyscan.io',
        # 'Connection': 'keep-alive',
        # 'Referer': 'https://www.proxyscan.io/',
        # 'Cookie':   'gads=ID=42433e12181887a0-222b39cfadc70007:T=1619783477:RT=1619783477:S=ALNI_MbNlXT_dDhRZIaeENkIJ8jQUTxVJg',
        # 'DNT': '1',
        # 'Sec-GPC': '1'
    }

    data = {
        'limit' : '800',
        "selectedCountry": country,
        "ping": "",
        "selectedType": proxy_args[proxy_type],
        "SelectedAnonymity": security_args[security_type],
        "sortPing": "false",
        "sortTime": "true",
        "sortUptime": "false"
    }

    if country == 'all':
        del data['selectedCountry']
    if proxy_type == 'all':
        del data['selectedType']
    if security_type == 'all':
        del data['SelectedAnonymity']

    response = requests.post(host, headers=headers, params=data)
    soup = BS(response.content, "lxml")
    th_all = soup.find_all('th', {'scope':'row'})
    for th in th_all:
        IP.append(th.text + ':' + th.find_next_siblings()[0].text)
    
    print(len(IP))

start('all', 'all', 'all')

    # while True:
    #     if check_internet:
    #         response = requests.post(host, headers=headers, data=data)
    #         data_scrap = response.json()
    #         page = data['page']
            
    #         for ip_scrap in data_scrap['proxies']:
    #             IP.append(ip_scrap['ip']+':'+str(ip_scrap['port']))

    #         if page == 3:
    #             break

    #         data['page'] += 1


    # return IP
