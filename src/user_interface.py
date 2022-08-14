from pyautogui import size
from msvcrt import getwch
from os import system, path, get_terminal_size as _size
from threading import Thread
from color_interpreter import _style

_abs_ = path.dirname(path.abspath(__file__)) #path to file

class wm_geometry:
    def __init__(self, width, height): self.width, self.height = width, height #width & height in columns & rows

geometry=wm_geometry(_size().columns, _size().lines)

'''
could be used dynamically by initializing a __new__ class everytime the scale changes(dimensions)
works by offesting a value from globals() by deriving the scale values from the geometry class
i fear it might be a little slow tho xd will see cba
'''

class ASCII_TABLE():
    CTRL_Q=chr(17)

ascii=ASCII_TABLE()

class HTML_INTERPRETER:
    def __new__(cls, *args, **kwargs) -> ...: ...
    def __init__(self) -> ...: ...

    '''
    will take the html of a page requested by the get() in requests.py
    request and will integrate it into the console ui system
    '''

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

def _dimensions(_string) -> ...:
    geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
    geometry.__init__(_size().columns, _size().lines)
    width=geometry.__dict__['width']; height=geometry.__dict__['height']
    _wrap(_string, **geometry.__dict__)
    while True:
        geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
        geometry.__init__(_size().columns, _size().lines)
        __width__, width = width, geometry.__dict__['width']
        __height__, height = height, geometry.__dict__['height']
        if width!=__width__ or height!=__height__:
            system('cls')
            _wrap(_string, **geometry.__dict__)


def _keydetection() -> ...: 
    while True: system('taskkill /f /im python.exe') if getwch()==ascii.CTRL_Q else None #chr(17) = &CTRL-Q
            

detection=Thread(target=_dimensions, args=('Main Page',)); detection.start()
keydetection=Thread(target=_keydetection); keydetection.start()