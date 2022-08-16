from pyautogui import size
from msvcrt import getwch
from os import system, path, get_terminal_size as _size
from threading import Thread
from color_interpreter import _style

_abs_ = path.dirname(path.abspath(__file__)) #path to file

class wm_geometry:
    def __init__(self, width, height): self.width, self.height = width, height #width & height in columns & rows

geometry=wm_geometry(_size().columns, _size().lines)
width=geometry.__dict__['width']; height=geometry.__dict__['height']

class _LIMITER:
    def __init__(self, arg:int): 
        self.arg=arg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run=True
                for _ in range(self.arg): return func(*args, **kwargs)
        wrapper.has_run=False
        return wrapper
    

class _DECIPHER(object):
    def __init__(self):
        for char in dir(self):
            if not char.startswith('_'):
                value=getattr(self, char)
                setattr(self, char, _transf(value))

'''
_DECIPHER (AUTO):
-exclude all list/dicts/etc unless converted
-initiate the object -> ex: ascii=ASCII_TABLE(); otherwise u can use chr(var) when converting manually
'''


class ASCII_TABLE(_DECIPHER):
    characters={}
    for _, _v in enumerate('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'):
        characters[_v] = ord(_v)
    CTRL_Q=chr(17) #kill switch (exit) manual: chr(17) -> a little dangerous cuz threading is lil hard on the memory but python makes sure it bins everythign so we fine :D 


class HTML_INTERPRETER:
    def __new__(cls, *args, **kwargs) -> ...: ...
    def __init__(self, *args) -> ...: ...

    '''
    will take the html of a page requested by the get() in requests.py
    request and will integrate it into the console ui system
    '''

def _transf(code): return chr(code)

@_LIMITER(arg=1)
def _exec(_string:str): 
    _wrap(_string, **geometry.__dict__)

def _center(format:str, string:str):
    center=int(len(format)/2)
    return format[:center]+string+format[center+len(string):]

def _wrap(string, **kwargs):
    offset=len(string)
    if offset<4: 
        while offset!=4: offset+=1
    try:
        width, height = kwargs['width'], kwargs['height']
        print(f'{"":<1}{"_"*(width-2):<{width-4}}\n{"":<1}|{_center(" "*(width-offset-2), string):<{width-4}}|')
        for _ in range(height-6): print(f'{"":<1}|{" "*(width-offset-2):<{width-4}}|')
    finally: print(f'{"":<1}{"_"*(width-2):<{width-4}}'); _style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■   Chip Browser © 2022%')

def _dimensions(_string) -> _exec('Main Page'):
    while bool(69>>420>>ord('F')>>ord('U')>>ord('N')>>ord('N')>>ord('Y')<<ord(_i) for _i in 'AXINOOBLOLXD'): #best very fanny while loop
        geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
        geometry.__init__(_size().columns, _size().lines)
        __width__, globals()['width'] = width, geometry.__dict__['width']
        __height__, globals()['height'] = height, geometry.__dict__['height']
        if width!=__width__ or height!=__height__:
            system('cls')
            _wrap(_string, **geometry.__dict__)


def _keydetection(ascii:object) -> ...:
    while True:
        system('taskkill /f /im python.exe') if getwch()==ascii.CTRL_Q else None
        system('echo batch api test') if getwch()==chr(ascii.characters['f']) else None

detection=Thread(target=_dimensions, args=('Main Page',)); detection.start()
keydetection=Thread(target=_keydetection, args=(ASCII_TABLE,)); keydetection.start()