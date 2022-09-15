import requests
from core.compatible import check_internet

#finish
def start(proxy_type, security_type, country):
    """
    takes all default args in start 

    Args: 
        mentioned in default config(not required)

    Return:
        array of tuple [('proxy_type', 'proxy')]

    """

    #return None #for debug

    IP = []

    proxy_args = {
        'all': [['http','all'],'socks4','socks5'],
        'http': [['http','all']],
        'http-only': [['http','no']],
        'https': [['http','yes']],
        'socks': ['socks4','socks5'],
        'socks4': 'socks4',
        'socks5': 'socks5',
    }

    security_args = {
        'all': 'all',
        'low': 'transparent',
        'average': 'anonymous',
        'high': 'elite'
    }

    host = 'https://api.proxyscrape.com/v2/'

    params = {
        'protocol':proxy_args[proxy_type],
        'anonymity':security_args[security_type],
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }

    if check_internet:
        if isinstance(params['protocol'],list):
            if len(params['protocol'])==1:
                params['ssl'] = params['protocol'][0][1]
                IP += scrap_ip(host, params['protocol'][0][0], params, headers)

            if len(params['protocol'])==2:
                if params['anonymity'] == 'all' or params['anonymity'] == 'elite':
                    params.pop('anonymity')
                    for i in params['protocol']:
                        IP += scrap_ip(host, i, params, headers)
            if len(params['protocol'])==3:
                for i in params['protocol']:
                    if isinstance(i,list):
                        params['ssl'] = i[1]
                        IP += scrap_ip(host, i[0], params, headers)
                    else:
                        try:
                            params.pop('anonymity')
                        except KeyError:
                            continue
                        IP += scrap_ip(host, i, params, headers)
        else:
            if params['anonymity'] == 'all' or params['anonymity'] == 'elite':
                print('here')
                params.pop('anonymity')
                IP += scrap_ip(host, params['protocol'], params, headers)

    return IP

def scrap_ip(host, ptype, addparam, headers):

    params = {
        'request': 'getproxies',
        'timeout': '10000',
        'country': 'all',
        'simplified': 'true',
    }

    params.update(addparam)
    params['protocol'] = ptype

    #print(params)
    response = requests.get(host, params=params, headers=headers)
    #print(response.text)
    if response.status_code==200:
        IP = response.text.strip().split('\r\n')
        return IP
    #print(len(IP))
    return []
    