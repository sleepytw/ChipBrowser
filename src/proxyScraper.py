from bs4 import BeautifulSoup
import requests, json, random as r

data=json.load(open('requestsData.json'));

def parse():
    proxies=([{_p: _i} for _p in data['proxies'] for _i in data['proxies'][_p]])
    page=requests.get(''.join([_u for _u in r.choice(data['conns'])]), headers=data['headers'], proxies=r.choice(proxies) if proxies else None);
    print(f'{(page.status_code, page.content)}')
