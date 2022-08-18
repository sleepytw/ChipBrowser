import json, os, importlib, socket

from color_interpreter import Fore, Back, Style, _style
from json_dump import *


class EmptyException(Exception): pass
os.system("")

'''
TODO:
-> POST REQUESTS (AUTH/2, COOKIES ETC)
-> parse http headers received and spit them into .text(); .content(); .headers() etc
-> redirect site detection (from scratch)
-> http to https conn compatibility {being able to connect to https sites whilst sending http requests} (from scratch) POST & GET
-> proxy E2EE encryption (from scratch)
'''

path = os.path.dirname(os.path.abspath(__file__)) #path to file
_ext=path.replace('src', 'ext') # path to prev parent dir

#_style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■\n%')

rdata, data = (json.load(open(values)) for (_, values) in enumerate([f'{_ext}\\requests_data.json', f'{_ext}\\data.json']))

def _get(
    _requirements: ...,
    _url: ...,
    _params: ...,
    _data: ...,
    _headers: ...,
    _cookies: ...,
    _files: ...,
    _auth: ...,
    _timeout: ...,
    _allow_redirects: ...,
    _proxies: ...,
    _hooks: ...,
    _stream: ...,
    _verify: ...,
    _cert: ...,
    _json: ...
) -> str:  return [bool(type(_u16)) for _u16 in locals().values()]

def _post(
    _requirements: ...,
    _url: ...,
    _data: ...,
    _json: ...,
    _params: ...,
    _headers: ...,
    _cookies: ...,
    _files: ...,
    _auth: ...,
    _timeout: ...,
    _allow_redirects: ...,
    _proxies: ...,
    _hooks: ...,
    _stream: ...,
    _verify: ...,
    _cert: ...,
) -> str: return [bool(type(_u15)) for _u15 in locals().values()]

'''/ bool.check to make sure that the requirements are the same as the ones given after initial execution but idk might not need it will see/'''

def _http(
    _method: str, #"POST" | "GET"
    _path: str, #/hidden.html
    _version: str, #"HTTP /1.0" | "HTTP /1.1"
    _host: str, #localhost:8000
    _agent: dict, #globals()[data]['headers'],
    _connection: str,
    _contentLength: int
) -> None: return [bool(type(_u6)) for _u6 in locals().values()] #def of a get&post req params after http parsing

def validate(file, _cache='__ERROR') -> locals():
    """ Check if file is empty by confirming if its size is 0 bytes"""
    return os.path.exists(f'{file}.py') and os.stat(f'{file}.py').st_size == 0

def modules(_c: list) -> ...: #_c ~ cache {initialize([]);}
    try:
        for _m in data['modules']:
            if validate(_m): _c.append(_m)
            else: globals()[_m] = importlib.import_module(_m); #-> also make it list all functions and desc or wahtever the fuck
        if len(_c)!=0: raise EmptyException
        else: return None
    except EmptyException:
        print(f"""Unimported module/s:\n{['%s' % _i for _i in _c]}""")

def get(    
    _address: tuple, #dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    _path: str, #/hidden.html; /ip; /search or whatever
    #_cookie: str,
    _proxy: tuple, #init proxy address&port (...)
) -> str:
    _http=f"GET /{_path} HTTP/1.1\r\nHost: {_address[0]}\r\n{''.join(rdata['headers'])}: {''.join(rdata['headers']['User-Agent'])}\r\nConnection: keep-alive\r\n\r\n"
    #\r\nCookie: {_cookie}\r\nContent-Length: {len(_cookie)}\r\n\r\n"
    #_style.beautify(f'&BRIGHT@%&LIGHTGREEN_EX@[SEND]\n%&RESET@%&LIGHTRED_EX@{_http}%&RESET@%')
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM); #-- HTTP onto TCP/IP
    sock.connect(_proxy);
    sock.sendall(_http.encode())
    response=sock.recv(8192)
    sock.close()
    #_style.beautify(f'&BRIGHT@%&LIGHTGREEN_EX@[RECV]\n%&RESET@%&CYAN@{response.decode()}%&RESET@%')
    return response.decode()

    #Connection: keep-alive\r\n #HTTP/1.1 default behaviour, but "close" can be used to mimic the HTTP/1.0 behaviour

    __ALTERNATIVE__= "{socket.gethostbyname(_address[0]) if (_address[0]==str() and \
    ('www' or 'http://' or 'https://') in _address[0]) \
    else _address[0]}:{_address[1]}\r\n"

    '''
    baiscally what hgapepns in the shitty hardcoded bullshit above is it conncets to a proxy and prays
    that it redirects the http msg sent to the proxy, to the site we're tryna reach
    sorry fucko ur 1for2 
    '''

    '''
    hopefully my reptile brain will remember to hash and encrypt the info im sending out 
    to the proxy cuz with free proxies and encrypt the latter cuz
    its kinda not very safe hhaha xD
    '''

#response=get(('httpbin.org', 80), 'ip', ('103.117.192.14', 80))

def post(
    _address: tuple, #dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    _path: str,
    _cookie: str,
    _auth: str,
    _proxy: tuple, #init proxy address&port
) -> str:
    _http=f"POST /{_path} HTTP/1.1\r\nHost: {_address[0]}\r\n{''.join(rdata['headers'])}: {''.join(rdata['headers']['User-Agent'])}\r\nConnection: keep-alive\r\nCookie: {_cookie}\r\nContent-Length: {len(_cookie)}\r\n\r\n"
    _style.beautify(f'&BRIGHT@%&LIGHTGREEN_EX@[SEND]\n%&RESET@%&LIGHTRED_EX@{_http}%&RESET@%')
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM); #-- HTTP onto TCP/IP
    sock.connect(_proxy);
    sock.sendall(_http.encode())
    response=sock.recv(8192)
    sock.close()
    _style.beautify(f'&BRIGHT@%&LIGHTGREEN_EX@[RECV]\n%&RESET@%&CYAN@{response.decode()}%&RESET@%')
    return response.decode()

#post(('testphp.vulnweb.com', 80), 'login.php', 'login=test%2Ftest', ..., ('103.117.192.14', 80))

'''
relation ->
POST /notes.html HTTP/1.1\r\nContent-Length: 30\r\nCookie: username=sleepyxd; password=urmom123\r\n\r\naction=addNote&input=["index{i}"]'.encode()
method; url; param; content-length; cookies; auth; verify; action within the browser or whatever tf
'''

def _pseudo(
    _address: ...,
    _proxy: ...
    ) -> None: socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((..., ...)); #-- HTTP onto TCP/IP