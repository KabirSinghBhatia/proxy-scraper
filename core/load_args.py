import argparse
import sys
from core.default_config import default_configs

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def load_all_args(module_name):

    default_configlist = default_configs()
    
    proxy_type_help = '''R|Available options are: 
            1. http (contains http and https)
            2. http-only
            3. https
            4. socks (contains socks4 and socks5)
            5. socks4
            6. socks5
            7. all
            '''

    proxy_security_help = '''R|Available options are: 
            1. low
            2. average
            3. high'''
    
    #Start parser
    parser = argparse.ArgumentParser(add_help=True,formatter_class=SmartFormatter)

    #proxy options

    proxyOpt = parser.add_argument_group("Proxy","Proxy options")

    proxyOpt.add_argument("-c","--country",action="store", 
                            dest="country", 
                            default=default_configlist["country"], 
                            help="write country code by using parameter (Under development) e.g: --country US")

    proxyOpt.add_argument("-p","--proxy_type",action="store", 
                            dest="proxy_type", 
                            default=default_configlist["proxy_type"], 
                            help=proxy_type_help)

    proxyOpt.add_argument("-s","--security_type",action="store", 
                            dest="security_type", 
                            default=default_configlist["security_type"], 
                            help=proxy_security_help)
    
    features = parser.add_argument_group("features","additional options")
    
    features.add_argument("--remove-dead",action="store_true", 
                            dest="remove_dead", 
                            default=default_configlist["remove-dead"], 
                            help='''R|--remove-dead filters dead proxy(may contains false positive). 
                            Using this can take longer time''')
    '''
    #request options
    requestOpt = parser.add_argument_group("Requests","Request type")

    requestOpt.add_argument("-H","--headers",action="store", 
                            dest="headers",default=default_configlist["headers"], 
                            help="providing additional headers in dict or json format")
    
    requestOpt.add_argument("-C","--cookies",action="store", 
                            dest="cookies",default=default_configlist["cookies"], 
                            help="providing cookies")
    '''

    return [parser,parser.parse_args()]

def validate_all_required(proxy_type, security_type, country, remove_dead):
    
    valid_proxy_type = [
        'http',
        'http-only',
        'https',
        'socks',
        'socks4',
        'socks5',
        'all'
    ]

    valid_security_type = [
        'low', 'medium', 'high', 'all'
    ]

    if proxy_type == '':
        print("enter proxy type")
        sys.exit(1)
    elif proxy_type not in valid_proxy_type:
        print("enter valid proxy type")
        sys.exit(1)
    
    if security_type not in valid_security_type:
        print("enter valid security type")
        sys.exit(1)

    return proxy_type, security_type, country, remove_dead