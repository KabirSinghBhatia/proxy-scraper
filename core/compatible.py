import os
import sys
import requests
from datetime import datetime

#get os the name
#check for windows (for better path traversal)
#check for python version (support only 3)
#logo for proxy-grabber


def os_name():
    """
    OS name

    Returns:
        OS name in string
    """
    return sys.platform

def is_windows():
    """
    check if the framework run in Windows OS

    Returns:
        True if its running on windows otherwise False
    """
    if 'win32' == os_name() or 'win64' == os_name():
        return True
    return False

def version():
    """
    version of python

    Returns:
        integer version of python (2 or 3)
    """
    return int(sys.version_info[0])

def check_internet():
    """
    check iternet connection 

    Returns:
        True or False
    """
    
    if requests.get('https://google.com').status_code==200:
        return True
    return False

def logo():
    return '''
    ____                           _____                                
   / __ \_________  _  ____  __   / ___/______________ _____  ___  _____
  / /_/ / ___/ __ \| |/_/ / / /   \__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/
 / ____/ /  / /_/ />  </ /_/ /   ___/ / /__/ /  / /_/ / /_/ /  __/ /    
/_/   /_/   \____/_/|_|\__, /   /____/\___/_/   \__,_/ .___/\___/_/     
                      /____/                        /_/                 

        - Divyansh Jain
        - Kabir Singh Bhatia
    '''

def output_to_file(proxy_list=[], filename=datetime.now().strftime("%d%m%Y%H%M%S")):
    filename += ".txt"
    try:
        os.mkdir('proxy_lists')
    except FileExistsError:
        pass
    filepath =  os.path.join('proxy_lists',filename)
    with open(filepath, 'w') as out_file:
        for proxy in proxy_list:
            out_file.write(proxy + '\n')
    
    print('Your proxylist has been stored as ' + os.path.join(os.getcwd(),filepath))