import socket, os

from color_interpreter import _style


os.system("")

_server=('127.0.0.1', 2323); _redirect=f'{_server[0]}:{_server[1]}/index.html'
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(_server)
sock.listen()
_style.beautify('&LIGHTGREEN_EX@[EST]\n%&LIGHTMAGENTA_EX@-> WAITING FOR CONNECTIONS\n\n%&RESET@%')
conn, addr = sock.accept()

while True:
    _msg=conn.recv(4096).decode()
    print(_msg)
    if _msg!='':
        conn.sendall(f"HTTP/1.1 301 Moved Permanently\r\nContent_Length: 0\r\nConnection: close\r\nLocation: {_redirect}\r\n\r\n".encode())
        break