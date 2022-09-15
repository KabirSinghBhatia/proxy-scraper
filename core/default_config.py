#dictionary written on top for every default argument

headers = {
    #'Host': 'hidemy.name',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Language': 'en-US,en;q=0.5',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Connection': 'keep-alive',
    #'Cookie': '__cfduid=d6c29c886819d92283f66b1b2a69528a71606222113',
    #'Upgrade-Insecure-Requests': '1'
}


def default_configs():
    """
    all default configuration are here

    Returns:
        dict with all user configs
    """

    return {
        "headers": headers,
        "cookies": None,
        "remove-dead": False,
        "proxy_type": "",
        "security_type": "all",
        "country": "all"
    }