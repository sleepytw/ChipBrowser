import json, os, importlib, socket
from abc import ABC, abstractmethod
import ssl

from ChipEngine.color_interpreter import Fore, Back, Style, _style
from ChipEngine.json_dump import *
import ChipVPN.RSA_Encryption as rsa


class EmptyException(Exception):
    pass


os.system("")


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
    address  : tuple,  # dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    proxy    : tuple,  # init proxy address&port (...)
    _path    : str  # /hidden.html; /ip; /search or whatever

) -> str:

    headers = """\
GET /{path} HTTP/1.1\r\n\
Host: {host}\r\n\
User-Agent: {user_agent}\r\n\
Connection: keep-alive\r\n\r\n"""

    payload = headers.format(
        path       = _path,
        host       = address[0],
        user_agent = {''.join(rdata['headers']['User-Agent'])}
    ).encode()

    # -- HTTP onto TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        if proxy[0] == "127.0.0.1":
            sock.connect(address)
        
        sock.connect(proxy)

        if address[1] == 443:
            context = ssl.create_default_context()
            sock    = context.wrap_socket(sock, server_hostname=address[0])

        sock.sendall(payload)
        response = sock.recv(65555)

    return response.decode()


def post(

    address  : tuple,  # dst.address&port (if dst.ip is a domain it will convert it to ip format else ...)
    proxy    : tuple,  # init proxy address&port (...)
    _path    : str,  # /hidden.html; /ip; /search or whatever
    _payload : str

) -> str:

    headers = """\
GET /{path} HTTP/1.1\r\n\
Host: {host}\r\n\
Content-Type: {content_type}\r\n\
Content-Length: {content_length}\r\n\
User-Agent: {user_agent}\r\n\
Connection: keep-alive\r\n\r\n"""


    body_bytes = _payload.encode('ascii')
    header_bytes = headers.format(
        path           = _path,
        host           = address[0],
        content_type   = "application/x-www-form-urlencoded",
        content_length = len(body_bytes),
        user_agent     = {''.join(rdata['headers']['User-Agent'])}
    ).encode()

    payload = header_bytes + body_bytes

    # -- HTTP onto TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        if proxy[0] == "127.0.0.1":
            sock.connect(address)
        
        sock.connect(proxy)

        if address[1] == 443:
            context = ssl.create_default_context()
            sock    = context.wrap_socket(sock, server_hostname=address[0])

        sock.sendall(payload)
        response = sock.recv(65555)

    return response.decode()

def _pseudo(
    _address : ..., 
    _proxy   : ...
) -> None:

    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((..., ...))
    # -- HTTP onto TCP/IP


"""
IMPORTANT NOTE! ADD :
if __name__ == '__main__' ~~~

OTHERWISE INITIALLIZING THE REQUESTS BARE IS GONNA OVERLAP ON TOP OF THE MAIN FILE & ACTIVATE IT 2 TIMES LEADING TO DESCREPENCIES
"""