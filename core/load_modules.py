import sys
import os
import shutil
import inspect
import proxy_modules
from glob import glob
from core.compatible import is_windows

#load all internal modules
#load all external library (check for it)


def load_all_modules():
    """
    load all available modules

    Returns:
        an array of all module names
    """

    #search for modules
    module_names = []

    for module_path in glob(os.path.dirname(inspect.getfile(proxy_modules))+ '/*/engine.py'):
        """
        proxy_modules get file gets init.py 
        then at moment get dirname using glob 
        find regex pattern matching to that
        """
        module_name = module_path.rsplit('\\' if is_windows() else '/')[-2]
        module_names.append(module_name)
    return module_names

def load_external_modules():
    """
    check external libraries if they are installed

    Returns:
        True if success otherwise None
    """

    external_modules = ["argparse","requests","os","sys","beautifulsoup","proxy_checker"]

    for module in external_modules:
        try:
            __import__(module)
        except:
            print("install module "+module)
        
    return True
