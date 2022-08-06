import json, os, importlib, socket
class EmptyException(Exception): pass

def _get(
    _requirements: ...,
    _url: ...,
    _params: ..., *_args,
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
) -> None: return [bool(_ for _ in locals()['_requirements'])]

def _post(
    _requirements: ...,
    _url: ...,
    _data: ...,
    _json: ..., *_args,
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
) -> None: return [bool(_ for _ in locals()['_requirements'])]

'''/ bool.check to make sure that the requirements are intact before execution but idk might not need it will see/'''


def _http(_: ...) -> None: ... #def of a get&post req params after http parsing

def validate(file):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    return os.path.exists(f'{file}.py') and os.stat(f'{file}.py').st_size == 0

def modules(_c=None): #_c ~ cache
    data=json.load(open('data.json')); _c=list();
    try:
        for _m in data['modules']:
            if validate(_m): _c.append(_m);
            else: globals()[_m] = importlib.import_module(_m); #-> also make it list all functions and desc or wahtever the fuck
        if len(_c)!=0: raise EmptyException
        else: return None
    except EmptyException:
        print(f"""Unimported module/s:\n{['%s' % _i for _i in _c]}""")

def get(_: ...): ...
def post(_: ...): ...

'''
relation ->
POST /notes.html HTTP/1.1\r\nContent-Length: 30\r\nCookie: username=sleepyxd; password=urmom123\r\n\r\naction=addNote&input=["index{i}"]'.encode()
method; url; param; content-length; cookies; auth; verify; action within the browser or whatever tf

btw making my own requests library cuz i have to be able to bypass cloudflare somehow yk yk and also encrypt the shit and udnerstnad how it works 
hml its 10am i need slep xD
'''

def _pseudo(
    _: ...
    ) -> None: socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((_, _)); #-- HTTP onto TCP/IP
