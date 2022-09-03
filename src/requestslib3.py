import json, os, importlib, socket
from abc import ABC, abstractmethod
import ssl

from ChipEngine.color_interpreter import Fore, Back, Style, _style
from ChipEngine.json_dump import *
import ChipVPN.RSA_Encryption as rsa


class EmptyException(Exception):
    pass


os.system("")

"""
TODO:
-> POST REQUESTS (AUTH/2, COOKIES ETC)
-> parse http headers received and spit them into .text(); .content(); .headers() etc
-> redirect site detection (from scratch)
-> http to https conn compatibility {being able to connect to https sites whilst sending http requests} (from scratch) POST & GET
-> proxy E2EE encryption (from scratch)
-> proxy chain
"""

path = os.path.dirname(os.path.abspath(__file__))  # path to file
main_path = os.path.dirname(path)

rdata, data = (
    json.load(open(values))
    for (_, values) in enumerate([f"{main_path}\\ext\\requests_data.json", f"{main_path}\\ext\\data.json"])
)


class http_blueprints(ABC):
    @abstractmethod
    def _get(
        _requirements    : ...,
        _url             : ...,
        _params          : ...,
        _data            : ...,
        _headers         : ...,
        _cookies         : ...,
        _files           : ...,
        _auth            : ...,
        _timeout         : ...,
        _allow_redirects : ...,
        _proxies         : ...,
        _hooks           : ...,
        _stream          : ...,
        _verify          : ...,
        _cert            : ...,
        _json            : ...,
    ) -> str:
    
        return (
            [
                bool(type(_u16))] for _u16 in locals().values()
            )

    @abstractmethod
    def _post(
        _requirements    : ...,
        _url             : ...,
        _data            : ...,
        _json            : ...,
        _params          : ...,
        _headers         : ...,
        _cookies         : ...,
        _files           : ...,
        _auth            : ...,
        _timeout         : ...,
        _allow_redirects : ...,
        _proxies         : ...,
        _hooks           : ...,
        _stream          : ...,
        _verify          : ...,
        _cert            : ...,
    ) -> str:

        return (
            [
                bool(type(_u15))] for _u15 in locals().values()
            )


    """/ bool.check to make sure that the requirements are the same as the ones given after initial execution but idk might not need it will see/"""

    @abstractmethod
    def _http(
        _method        : str,  # "POST" | "GET"
        _path          : str,  # /hidden.html
        _version       : str,  # "HTTP /1.0" | "HTTP /1.1"
        _host          : str,  # localhost:8000
        _agent         : dict,  # globals()[data]['headers'],
        _connection    : str,
        _contentLength : int,
    ) -> None:

        return (
            [
                bool(type(_u6))] for _u6 in locals().values()
            ) # def of a get&post req params after http parsing


def get(
    _address  : tuple,  # dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    _path     : str,  # /hidden.html; /ip; /search or whatever
    # _cookie : str,
    _proxy    : tuple,  # init proxy address&port (...)
) -> str:

    _http = f"GET /{_path} HTTP/1.1\r\nHost: {_address[0]}\r\n{''.join(rdata['headers'])}: {''.join(rdata['headers']['User-Agent'])}\r\nConnection: keep-alive\r\n\r\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- HTTP onto TCP/IP
    if _proxy[0] == "127.0.0.1":
        sock.connect(_address)
    else:
        sock.connect(_proxy)
    if _address[1] == 443:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=_address[0])
    sock.sendall(_http.encode())
    response = sock.recv(65555)
    sock.close()
    return response.decode()

    # Connection: keep-alive\r\n #HTTP/1.1 default behaviour, but "close" can be used to mimic the HTTP/1.0 behaviour

    """
    hopefully my reptile brain will remember to hash the info im sending out 
    to the proxy and encrypt the latter cuz with free proxies
    its kinda not very safe hhaha xD
    """


# response=get(('httpbin.org', 80), 'ip', ('103.117.192.14', 80))


def post(
    _address : tuple,  # dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    _path    : str,
    _cookie  : str,
    _auth    : str,
    _proxy   : tuple,  # init proxy address&port
) -> str:

    _http = f"POST /{_path} HTTP/1.1\r\nHost: {_address[0]}\r\n{''.join(rdata['headers'])}: {''.join(rdata['headers']['User-Agent'])}\r\nConnection: keep-alive\r\nCookie: {_cookie}\r\nContent-Length: {len(_cookie)}\r\n\r\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # -- HTTP onto TCP/IP
    if _proxy[0] == "127.0.0.1":
        sock.connect(_address)
    else:
        sock.connect(_proxy)
    if _address[1] == 443:
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=_address[0])
    sock.sendall(_http.encode())
    response = sock.recv(65555)
    sock.close()
    return response.decode()


# post(('testphp.vulnweb.com', 80), 'login.php', 'login=test%2Ftest', ..., ('103.117.192.14', 80))

"""
relation ->
POST /notes.html HTTP/1.1\r\nContent-Length: 30\r\nCookie: username=sleepyxd; password=urmom123\r\n\r\naction=addNote&input=["index{i}"]'.encode()
method; url; param; content-length; cookies; auth; verify; action within the browser or whatever tf
"""


def _pseudo(
    _address : ..., 
    _proxy   : ...
) -> None:

    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((..., ...))
    # -- HTTP onto TCP/IP
