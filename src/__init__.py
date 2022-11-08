# from VPN.proxyserver import *
# from VPN.encryption import * 

# from ENGINE.BLUEPRINTS.EXTERNAL.test_init import *

# #print([if ["function", "class"] in [globals()[str(y)] for y in [x for x in globals()]]])

# print(FUNCOBJ.__annotations__['return'][''])

import ENGINE.color_interpreter as COLORS
import ENGINE.json_dump as JSON_DUMP
import ENGINE.random_generator as RANDOM
import ENGINE.HTML_INTERPRETER.htmlparser as HTML
import ENGINE.NETWORKING.base_requests as requests

import GUI.user_interface as GUI # EXTREMELY GENERIC; WILL SECTION IT

import VPN.encryption as encryption
import VPN.proxyserver as proxyserver

from inspect import getmembers, isfunction  
from abc import ABC, abstractmethod
from typing import Type

assert globals()['__name__'] == "__main__", "bad 10 0 XDDDD"

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

    ) -> None:

        return (
            [
                bool(type(_u15))] for _u15 in locals().values()
            )


    """/ bool.check to make sure that the requirements are the same as the ones given after initial execution but idk might not need it will see/"""

    @abstractmethod
    def _http(
        _method        : str,
        _path          : str,
        _version       : str, 
        _host          : str, 
        _agent         : dict,
        _connection    : str,
        _contentLength : int,

    ) -> None:

        return (
            [
                bool(type(_u6))] for _u6 in locals().values()
            ) # def of a get&post req params after http parsing

#overheated
