from bs4 import BeautifulSoup
import requests, json, random as r

data=json.load(open('requestsData.json')); [data[[_i for _i in str(data.keys()[_i])]][-1]=str()]

def parse():
    page=requests.get([_u for _u in r.choice(data['conns']) if not _u=="null" in data['conns']], headers=data['headers'][0]);
    return page.status_code()
