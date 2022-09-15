import requests
from bs4 import BeautifulSoup as BS
from core.compatible import check_internet

#first get token
#less priority

def start(proxy_type, security_type, country):
    """
    takes all default args in start 

    Args: 
        mentioned in default config(not required)

    Return:
        array of tuple [('proxy_type', 'proxy')]

    """

    #return None #for debug

    token, cookies = token_cookie()
    host = 'https://www.proxydocker.com/en/api/proxylist/'

    proxy = []  #this is going to return as mentioned in function spec
    IP = [] #this contains ip:port list through scrape data
    # country_dict = {
    #     "AF":"Afghanistan",
    #     "AL":"Albania",
    #     "DZ":"Algeria",
    #     "AS":"American Samoa",
    #     "AD":"Andorra",
    #     "AO":"Angola",
    #     "AI":"Anguilla",
    #     "AQ":"Antarctica",
    #     "AG":"Antigua and Barbuda",
    #     "AR":"Argentina",
    #     "AM":"Armenia",
    #     "AW":"Aruba",
    #     "AU":"Australia",
    #     "AT":"Austria",
    #     "AZ":"Azerbaijan",
    #     "BS":"Bahamas",
    #     "BH":"Bahrain",
    #     "BD":"Bangladesh",
    #     "BB":"Barbados",
    #     "BY":"Belarus",
    #     "BE":"Belgium",
    #     "BZ":"Belize",
    #     "BJ":"Benin",
    #     "BM":"Bermuda",
    #     "BT":"Bhutan",
    #     "BO":"Bolivia, Plurinational State of",
    #     "BO":"Bolivia",
    #     "BA":"Bosnia and Herzegovina",
    #     "BW":"Botswana",
    #     "BV":"Bouvet Island",
    #     "BR":"Brazil",
    #     "IO":"British Indian Ocean Territory",
    #     "BN":"Brunei Darussalam",
    #     "BN":"Brunei",
    #     "BG":"Bulgaria",
    #     "BF":"Burkina Faso",
    #     "BI":"Burundi",
    #     "KH":"Cambodia",
    #     "CM":"Cameroon",
    #     "CA":"Canada",
    #     "CV":"Cape Verde",
    #     "KY":"Cayman Islands",
    #     "CF":"Central African Republic",
    #     "TD":"Chad",
    #     "CL":"Chile",
    #     "CN":"China",
    #     "CX":"Christmas Island",
    #     "CC":"Cocos (Keeling) Islands",
    #     "CO":"Colombia",
    #     "KM":"Comoros",
    #     "CG":"Congo",
    #     "CD":"Congo, the Democratic Republic of the",
    #     "CK":"Cook Islands",
    #     "CR":"Costa Rica",
    #     "CI":"Côte d'Ivoire",
    #     "CI":"Ivory Coast",
    #     "HR":"Croatia",
    #     "CU":"Cuba",
    #     "CY":"Cyprus",
    #     "CZ":"Czech Republic",
    #     "DK":"Denmark",
    #     "DJ":"Djibouti",
    #     "DM":"Dominica",
    #     "DO":"Dominican Republic",
    #     "EC":"Ecuador",
    #     "EG":"Egypt",
    #     "SV":"El Salvador",
    #     "GQ":"Equatorial Guinea",
    #     "ER":"Eritrea",
    #     "EE":"Estonia",
    #     "ET":"Ethiopia",
    #     "FK":"Falkland Islands (Malvinas)",
    #     "FO":"Faroe Islands",
    #     "FJ":"Fiji",
    #     "FI":"Finland",
    #     "FR":"France",
    #     "GF":"French Guiana",
    #     "PF":"French Polynesia",
    #     "TF":"French Southern Territories",
    #     "GA":"Gabon",
    #     "GM":"Gambia",
    #     "GE":"Georgia",
    #     "DE":"Germany",
    #     "GH":"Ghana",
    #     "GI":"Gibraltar",
    #     "GR":"Greece",
    #     "GL":"Greenland",
    #     "GD":"Grenada",
    #     "GP":"Guadeloupe",
    #     "GU":"Guam",
    #     "GT":"Guatemala",
    #     "GG":"Guernsey",
    #     "GN":"Guinea",
    #     "GW":"Guinea-Bissau",
    #     "GY":"Guyana",
    #     "HT":"Haiti",
    #     "HM":"Heard Island and McDonald Islands",
    #     "VA":"Holy See (Vatican City State)",
    #     "HN":"Honduras",
    #     "HK":"Hong Kong",
    #     "HU":"Hungary",
    #     "IS":"Iceland",
    #     "IN":"India",
    #     "ID":"Indonesia",
    #     "IR":"Iran, Islamic Republic of",
    #     "IQ":"Iraq",
    #     "IE":"Ireland",
    #     "IM":"Isle of Man",
    #     "IL":"Israel",
    #     "IT":"Italy",
    #     "JM":"Jamaica",
    #     "JP":"Japan",
    #     "JE":"Jersey",
    #     "JO":"Jordan",
    #     "KZ":"Kazakhstan",
    #     "KE":"Kenya",
    #     "KI":"Kiribati",
    #     "KP":"Korea, Democratic People's Republic of",
    #     "KR":"Korea, Republic of",
    #     "KR":"South Korea",
    #     "KW":"Kuwait",
    #     "KG":"Kyrgyzstan",
    #     "LA":"Lao People's Democratic Republic",
    #     "LV":"Latvia",
    #     "LB":"Lebanon",
    #     "LS":"Lesotho",
    #     "LR":"Liberia",
    #     "LY":"Libyan Arab Jamahiriya",
    #     "LY":"Libya",
    #     "LI":"Liechtenstein",
    #     "LT":"Lithuania",
    #     "LU":"Luxembourg",
    #     "MO":"Macao",
    #     "MK":"Macedonia, the former Yugoslav Republic of",
    #     "MG":"Madagascar",
    #     "MW":"Malawi",
    #     "MY":"Malaysia",
    #     "MV":"Maldives",
    #     "ML":"Mali",
    #     "MT":"Malta",
    #     "MH":"Marshall Islands",
    #     "MQ":"Martinique",
    #     "MR":"Mauritania",
    #     "MU":"Mauritius",
    #     "YT":"Mayotte",
    #     "MX":"Mexico",
    #     "FM":"Micronesia, Federated States of",
    #     "MD":"Moldova, Republic of",
    #     "MC":"Monaco",
    #     "MN":"Mongolia",
    #     "ME":"Montenegro",
    #     "MS":"Montserrat",
    #     "MA":"Morocco",
    #     "MZ":"Mozambique",
    #     "MM":"Myanmar",
    #     "MM":"Burma",
    #     "NA":"Namibia",
    #     "NR":"Nauru",
    #     "NP":"Nepal",
    #     "NL":"Netherlands",
    #     "AN":"Netherlands Antilles",
    #     "NC":"New Caledonia",
    #     "NZ":"New Zealand",
    #     "NI":"Nicaragua",
    #     "NE":"Niger",
    #     "NG":"Nigeria",
    #     "NU":"Niue",
    #     "NF":"Norfolk Island",
    #     "MP":"Northern Mariana Islands",
    #     "NO":"Norway",
    #     "OM":"Oman",
    #     "PK":"Pakistan",
    #     "PW":"Palau",
    #     "PS":"Palestinian Territory, Occupied",
    #     "PA":"Panama",
    #     "PG":"Papua New Guinea",
    #     "PY":"Paraguay",
    #     "PE":"Peru",
    #     "PH":"Philippines",
    #     "PN":"Pitcairn",
    #     "PL":"Poland",
    #     "PT":"Portugal",
    #     "PR":"Puerto Rico",
    #     "QA":"Qatar",
    #     "RE":"Réunion",
    #     "RO":"Romania",
    #     "RU":"Russian Federation",
    #     "RU":"Russia",
    #     "RW":"Rwanda",
    #     "SH":"Saint Helena, Ascension and Tristan da Cunha",
    #     "KN":"Saint Kitts and Nevis",
    #     "LC":"Saint Lucia",
    #     "PM":"Saint Pierre and Miquelon",
    #     "VC":"Saint Vincent and the Grenadines",
    #     "VC":"Saint Vincent & the Grenadines",
    #     "VC":"St. Vincent and the Grenadines",
    #     "WS":"Samoa",
    #     "SM":"San Marino",
    #     "ST":"Sao Tome and Principe",
    #     "SA":"Saudi Arabia",
    #     "SN":"Senegal",
    #     "RS":"Serbia",
    #     "SC":"Seychelles",
    #     "SL":"Sierra Leone",
    #     "SG":"Singapore",
    #     "SK":"Slovakia",
    #     "SI":"Slovenia",
    #     "SB":"Solomon Islands",
    #     "SO":"Somalia",
    #     "ZA":"South Africa",
    #     "GS":"South Georgia and the South Sandwich Islands",
    #     "ES":"Spain",
    #     "LK":"Sri Lanka",
    #     "SD":"Sudan",
    #     "SR":"Suriname",
    #     "SJ":"Svalbard and Jan Mayen",
    #     "SZ":"Swaziland",
    #     "SE":"Sweden",
    #     "CH":"Switzerland",
    #     "SY":"Syrian Arab Republic",
    #     "TW":"Taiwan, Province of China",
    #     "TW":"Taiwan",
    #     "TJ":"Tajikistan",
    #     "TZ":"Tanzania, United Republic of",
    #     "TH":"Thailand",
    #     "TL":"Timor-Leste",
    #     "TG":"Togo",
    #     "TK":"Tokelau",
    #     "TO":"Tonga",
    #     "TT":"Trinidad and Tobago",
    #     "TT":"Trinidad & Tobago",
    #     "TN":"Tunisia",
    #     "TR":"Turkey",
    #     "TM":"Turkmenistan",
    #     "TC":"Turks and Caicos Islands",
    #     "TV":"Tuvalu",
    #     "UG":"Uganda",
    #     "UA":"Ukraine",
    #     "AE":"United Arab Emirates",
    #     "GB":"United Kingdom",
    #     "US":"United States",
    #     "UM":"United States Minor Outlying Islands",
    #     "UY":"Uruguay",
    #     "UZ":"Uzbekistan",
    #     "VU":"Vanuatu",
    #     "VE":"Venezuela, Bolivarian Republic of",
    #     "VE":"Venezuela",
    #     "VN":"Viet Nam",
    #     "VN":"Vietnam",
    #     "VG":"Virgin Islands, British",
    #     "VI":"Virgin Islands, U.S.",
    #     "WF":"Wallis and Futuna",
    #     "EH":"Western Sahara",
    #     "YE":"Yemen",
    #     "ZM":"Zambia",
    #     "ZW":"Zimbabwe",
    # }

    # country = country if country=='all' else country_dict[country]

    proxy_args = {
        'all': 'all',
        'http': 'http-https',
        'http-only': 'http',
        'https': 'https',
        'socks': 'socks',
        'socks4': 'socks4',
        'socks5': 'socks5',
    }

    security_args = {
        'all': 'all',
        'low': 'TRANSPARENT',
        'average': 'ANONYMOUS',
        'high': 'ELITE'
    }


    headers = {
        'Host': 'www.proxydocker.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #'Accept-Language': 'en-US,en;q=0.5',
        #'Accept-Encoding': 'gzip, deflate, br',
        #'Connection': 'keep-alive',
        #'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.proxydocker.com',
        #'Referer': 'https://www.proxydocker.com/en/proxylist/search?need=all&type=https&anonymity=ELITE&port=&country=&city=&state=all',
        #'Cookie':'AWSALB=MS63ShVyT5UOcMzgJ5kl769rZJQi2f0rqmk9iAY6WgGtymPwThM1h2l366Pgmlnxe1HOmtko1AEJbSZf+0M8YTgOai1paqiFNs5n8mmZleVD9Rtc5y3zHircuF7m; AWSALBCORS=MS63ShVyT5UOcMzgJ5kl769rZJQi2f0rqmk9iAY6WgGtymPwThM1h2l366Pgmlnxe1HOmtko1AEJbSZf+0M8YTgOai1paqiFNs5n8mmZleVD9Rtc5y3zHircuF7m; PHPSESSID=h7rt8uib1d3qk1766d05api576',
        'Cookie': f"AWSALB={cookies['AWSALB']}; AWSALBCORS={cookies['AWSALBCORS']}; PHPSESSID={cookies['PHPSESSID']}",
        #'TE': 'Trailers',
        #'Pragma': 'no-cache',
        #'Cache-Control': 'no-cache',
    }

    data = {
        'token': token,
        'country': 'all',
        'city':'all',
        'state':'all',
        'port':'all',
        'type': proxy_args[proxy_type],
        'anonymity':security_args[security_type],
        'need':'all',
        'page':1
    }

    if country != 'all':
        data['country'] = country

    while True:
        if check_internet:
            response = requests.post(host, headers=headers, data=data)
            data_scrap = response.json()
            page = data['page']
            
            for ip_scrap in data_scrap['proxies']:
                IP.append(ip_scrap['ip']+':'+str(ip_scrap['port']))

            if page == 3:
                break

            data['page'] += 1


    return IP


def token_cookie():
    """
    Get the valid token from the page and then use it for scraping this site.

    Args:
        NO args

    Return:
        token and cookie of the site
    """

    host = 'https://www.proxydocker.com/'

    response = requests.get(host)
    token_scrap = BS(response.text,'lxml')
    return token_scrap.find('meta', {'name':'_token'})['content'], response.cookies
