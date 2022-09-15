import requests
from core.compatible import check_internet


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
        'all': ['http','https','socks4','socks5'],
        'http': ['http','https'],
        'http-only': 'http',
        'https': 'https',
        'socks': ['socks4','socks5'],
        'socks4': 'socks4',
        'socks5': 'socks5',
    }

    security_args = {
        'all': 'all',
        'low': 'Transparent',
        'average': 'Anonymous',
        'high': 'Elite'
    }

    host = 'https://www.proxy-list.download/api/v0/get'

    headers = {}

    params = {
        't':proxy_args[proxy_type]
    }

    if check_internet:
        response = []
        if isinstance(params['t'],list) :
            for i in params['t']:
                response += scrap_ip(host,i,headers)
        else:
            response += scrap_ip(host, params['t'], headers)  

    for i in response:

        if security_args[security_type] == 'all':
            IP.append(i['IP']+':'+i['PORT'])
        
        elif security_args[security_type] == i['ANON']:
            IP.append(i['IP']+':'+i['PORT'])

    return IP

def scrap_ip(host, ptype, headers):

    params = {
        'l': 'en',
        't': ptype,
    }

    response = requests.get(host,params=params)
    if response.status_code==200:
        data = response.json()
        ip_scrap = data[0]["LISTA"]
        return ip_scrap

    return []