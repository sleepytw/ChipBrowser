from bs4 import BeautifulSoup
import requests, json, random as r

rdata=json.load(open('requestsData.json'));

def _analyze(_: ...) -> None:
    proxies=([{_p: _i} for _p in rdata['proxies'] for _i in rdata['proxies'][_p]])
    response=requests.get(''.join([_u for _u in r.choice(rdata['conns'])]), headers=rdata['headers'], proxies=r.choice(proxies) if proxies else None);
    return response.json() if rdata['conns'][0] == "https://httpbin.org/ip" else ...

def _parse(_resp: _analyze(...)):
    print(_resp);

_parse(_analyze(...));