import socket
import ssl

import RSA_Encryption as rsa


class Encryption(object):
    
    '''
    ---Encryption---

    RSA for numbers, 
    hence => Other encryption + number encryption seperated with %% 
    For instance:
    Ht934089th0fh0iEHGF)*h3408t320rtjf-93=t0f234=0t-932t=03jt-fnj0ib3028fh23-$    %numbers%     0h4308gh043g0-34-gj34-9fgj-we[ojkfgj3480-gn34-e]

    %numbers% RSA;
    evrything else sha256 for example idk xD

    encrypt, all attributes like src/dst_ip to prevent MITM attacks leading to DDOS attacks & other exploits
    '''

    '''
    scheme:

    client (encrypt) -> vpn server (decrypt) -> redirect to webserver -> recv from webserver -> vpn server (encrypt, response) -> client (decrypt, final)
    '''

    @classmethod
    def encrypt(cls): ...


class Proxy(object):

    def __init__(self, config: dict = {}, buffer_size: int = 0):

        self.__clients   = {}
        self.config      = config
        self.buffer_size = buffer_size

    def receive(self, response, src_pub_ip, src_ip, dst_ip, url, payload, port: int = 69420) -> ...: #port for host doesnt matter
        
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((self.config['HOST_NAME'], self.config['BIND_PORT']))
        
        self.server.listen(10) # handling max 10 connections

        self.client_response = self.server.recv(self.buffer_size).decode().split(';')
        self.src_public_ip, self.src_ip, self.dst_ip, self.dst_url, self.payload, self.port = self.client_response #dst_ip -> domain to ipv4
        self.server.sendall(Proxy.redirect(), port_web = 80)

    def redirect(self, port_web: int = 80) -> str: #default http port 80
        
        redirect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        redirect.connect((self.dst_url, port_web))
        #if the port is 443 https, dont encrypt, data already encrypted
        if self.port == 443:
            context  = ssl.create_default_context()
            redirect = context.wrap_socket(redirect, server_hostname=self.dst_url)
        redirect.sendall(self.payload.encode())
        redirect_response = redirect.recv(self.buffer_size)
        redirect.close()
        return redirect_response.decode()
