import json, os, importlib, socket

from ChipEngine.color_interpreter import Fore, Back, Style, _style
from ChipEngine.json_dump import *

# directly import the gui will execute every line therefore running the gui, doing this instead of initializing the code here cuz kkidna boring idkx D
import user_interface


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
"""

path = os.path.dirname(os.path.abspath(__file__))  # path to file
main_path = os.path.dirname(path)


_style.beautify(
    "&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■\n%"
)

rdata, data = (
    json.load(open(values))
    for (_, values) in enumerate([f"{main_path}\\ext\\requests_data.json", f"{main_path}\\ext\\data.json"])
)


def validate(file, _cache="__ERROR") -> locals():
    """Check if file is empty by confirming if its size is 0 bytes"""
    return os.path.exists(f"{file}.py") and os.stat(f"{file}.py").st_size == 0


def modules(_c: list) -> ...:  # _c ~ cache {initialize([]);}
    try:
        for _m in data["modules"]:
            if validate(_m):
                _c.append(_m)
            else:
                globals()[_m] = importlib.import_module(_m)
                # -> also make it list all functions and desc or wahtever the fuck
        if len(_c) != 0:
            raise EmptyException
        else:
            return None
    except EmptyException:
        print(f"""Unimported module/s:\n{['%s' % _i for _i in _c]}""")
