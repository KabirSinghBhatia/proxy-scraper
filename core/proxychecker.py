import requests
import concurrent.futures
from core.compatible import check_internet
from proxy_checker import ProxyChecker

# def proxyscraper_checker(ip,port):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
#         'Content-Type': 'multipart/form-data; boundary=---------------------------137122606920925305691115849103'
#     }
#     host='https://onlinechecker.proxyscrape.com/index.php'
#     data = f'''-----------------------------137122606920925305691115849103
# Content-Disposition: form-data; name="ip_addr"

# {ip}
# -----------------------------137122606920925305691115849103
# Content-Disposition: form-data; name="port"

# {port}
# -----------------------------137122606920925305691115849103--'''
#     #print(data)
#     response = requests.post(host,data=data, headers=headers)
#     print(response.json())
#     return response.json()['working']

# def check_deadproxy(ip,port):
#     if check_internet:
#         if proxyscraper_checker(ip,port):
#             return True
#         return False
#     return False


def checking_proxy(proxy):
    
    checker = ProxyChecker()
    result = checker.check_proxy(proxy)

    if result:
        return proxy
    
    return False




def checking_proxies(proxy_list):
    
    valid_proxies = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(checking_proxy, proxy_list)
        
    for result in results:
        if result:
            valid_proxies.append(result)

    return valid_proxies


    

    