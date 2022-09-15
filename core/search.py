import importlib
from core.proxychecker import checking_proxies

def start_search(module_names, proxy_type, security_type, country, remove_dead):
    # print("great")
    proxies=[]

    for module in module_names:
        print(f"In the {module} module")
        library = importlib.import_module('proxy_modules.{0}.engine'.format(module))
        start = getattr(library, 'start')
        proxy = start(proxy_type, security_type, country)

        if proxy!=None:
            proxies+=proxy
            print(f"received {len(proxy)} from this module")
    print(f"we get total {len(proxies)} proxy")
    

    
    

    if remove_dead:
        valid_proxy = checking_proxies(proxies)    
        print(f"we get total {len(valid_proxy)} live proxy")
        return valid_proxy
    
    # for each in proxies:
    #     print(each)    

    return proxies