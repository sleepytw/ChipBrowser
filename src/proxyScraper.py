from bs4 import BeautifulSoup
import requests, json, random as r

data=json.load(open('requestsData.json'));

def parse():
    page=requests.get(''.join([_u for _u in r.choice(data['conns'])]), headers=data['headers'], proxies=''.join([_i for _i in r.choice(data['proxies'])]));
    print(f'{(page.status_code, page.content)}')

parse()
