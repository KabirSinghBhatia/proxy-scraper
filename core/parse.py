import sys
from core.compatible import logo
from core.compatible import output_to_file
from core.load_modules import load_all_modules
from core.load_args import load_all_args
from core.load_args import validate_all_required
from core.search import start_search

def run():
    """
    start intial execution by loading all args,modules, configs

    Returns:
        True if success otherwise None
    """
    print(logo())

    module_names = load_all_modules()  #list modules inside proxy modules
    #parse ARGVS

    # try:
    parser, options = load_all_args(module_names)
    # except SystemExit:
    #     print("ERRRRRROR")
    #     sys.exit(1)

    #filling args value

    #headers = options.headers
    #cookies = options.cookies
    proxy_type = options.proxy_type 
    security_type = options.security_type 
    country = options.country
    remove_dead = options.remove_dead

    #   sys.exit(0)
    #start search
    proxy_type, security_type, country, remove_dead = validate_all_required(
        proxy_type, security_type, country, remove_dead
    )

    # sys.stdout.flush()
    # #print('',flush=True)
    # sys.stdout.write("\r"+logo())
    # #sys.stdout.flush()

    proxy_list = start_search(module_names, proxy_type, security_type, country, remove_dead)

    output_to_file(proxy_list)

    return True