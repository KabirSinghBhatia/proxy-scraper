import requests



IP = [] #this contains ip:port list through scrape data

proxy_args = {
    'all': '',
    'http': 'hs',
    'http-only': 'h',
    'https': 's',
    'socks': 45,
    'socks4': 4,
    'socks5': 5,
}

security_args = {
    'all': '',
    'low': 12,
    'average': 3,
    'high':4
}

#temp
headers = {
    #'Host': 'hidemy.name',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Accept-Language': 'en-US,en;q=0.5',
    #'Accept-Encoding': 'gzip, deflate, br',
    #'Connection': 'keep-alive',
    # 'Cookie': '__cfduid=d718a12fb91e9654eb86438e3f61308111619250745; t=215478576; cf_clearance=d9f8c39f8055aa25b15a16d1c2e99f3c3bcb8226-1619250767-0-150',
    #'Upgrade-Insecure-Requests': '1'
}



host = 'https://hidemy.name/en/proxy-list/'
#print(host)

params = {
    'type': 'hs',                                   # proxy_args[proxy_type],      #for socks5
    'anon':  '3'                                 # security_args[security_type],      #for elite security
}

# if proxy_type == 'all':
#     params.pop('type')

# if security_type == 'all':
#     params.pop('anon')

# if country!='all':
#     params['country'] = country


# while True:
        
# print(headers['Cookie'])
response = requests.get(host,params=params,headers=headers)
print(response)
print(response.url)
#     if response.status_code==200:
#         data = BS(response.text,'lxml')
#         ip_scrap = data.tbody.find_all(['td'])
#         nxt_button = data.find('li',class_="next_array")

#         ln=len(ip_scrap)
#         skip=0

#         while skip<ln:
#             IP.append(ip_scrap[skip].text+':'+ip_scrap[skip+1].text)
#             skip+=7

#         if nxt_button == None:
#             break

#         if 'start' in params.keys():
#             params['start']+=64
#         else:
#             params['start']=64
    #print('proxy downloaded from HIDEmyname.')

# print(IP)