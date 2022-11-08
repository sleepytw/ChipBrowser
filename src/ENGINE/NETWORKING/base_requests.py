import json, os, importlib, socket
from abc import ABC, abstractmethod
import ssl




class EmptyException(Exception):
    pass


os.system("")


path = os.path.dirname(os.path.abspath(__file__))  # path to file
main_path = os.path.dirname(path)

rdata, data = (
    json.load(open(values))
    for (_, values) in enumerate([f"{main_path}\\ext\\requests_data.json", f"{main_path}\\ext\\data.json"])
)


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