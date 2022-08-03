from bs4 import BeautifulSoup
import requests, json, random as r

data=json.load(open('requestsData.json')); data['conns'][-1]=str()

def parse():
    page=requests.get([_u for _u in r.choice(data['conns']) if not _u=="null" in data['conns']], headers=data['headers'][0]);
    print(page.status_code())

parse()

"""
Traceback (most recent call last):
  File "C:\Users\-\Desktop\ChipBrowser\src\proxyScraper.py", line 10, in <module>
    parse()
  File "C:\Users\-\Desktop\ChipBrowser\src\proxyScraper.py", line 7, in parse
    page=requests.get([_u for _u in r.choice(data['conns']) if not _u=="null" in data['conns']], headers=data['headers'][0]);
KeyError: 0

supposed to select a random url from a url list from the json file listed as long as the choice isnt 'null', & headers[0] from the header var
"""