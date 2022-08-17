import re

from pyautogui import size
from msvcrt import getwch
from os import system, path, get_terminal_size as _size

from threading import Thread
from time import sleep

from color_interpreter import Fore, Back, Style, _style
from requestslib3 import get, post

response=re.split('\r\n',get(('httpbin.org', 80), 'ip', ('103.117.192.14', 80)))
for _i in response[-1].split('\n'): response.append(_i.strip())
del response[-5]

'''
braindead bandage solution for the http request problem idk what do hlep i cry T_T
'''

_abs_ = path.dirname(path.abspath(__file__)) #path to file

class InsufficientError(Exception): pass

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
            if not char.startswith('_') & char=='characters':
                value=getattr(self, char)
                setattr(self, char, _transf(value))

'''
_DECIPHER (AUTO):
-exclude all list/dicts/etc unless converted
-initiate the object -> ex: ascii=ASCII_TABLE(); otherwise u can use chr(var) when converting manually
'''


class ASCII_TABLE(_DECIPHER):
    characters={}
    for _, _v in enumerate('!"#$%&\'()*+,-./0123456789:;<=>?@ \
                            ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_` \
                            abcdefghijklmnopqrstuvwxyz{|}~'): characters[_v] = ord(_v)

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
def _load(_string:str):
    display(_attr=_string, _centered=True, **geometry.__dict__); sleep(2)

'''
_exec -> loading screen; replace sleep(2) -> loading time for all assets
'''

def _center(format:str, string:str):
    center=int(len(format)/2)
    #return format[:center]+f'{Fore.GREEN+string+Fore.RESET}'+format[center+len(string):] color
    return format[:center]+string+format[center+len(string):]

def _process(format:str, string:str):
    indent=int(len(format)/10)
    return format[:indent]+string+format[indent+len(string):]


def display(
    _attr:str or list, # list -> *strings
    _centered:bool,
    _index:int=0,
    _default:int=6,
    _last:int=4,
    **kwargs:dict
    ):
    system('cls')
    try:
        width, height = kwargs['width'], kwargs['height']
        top, bottom = f'{"":<1}{"_"*(width-2):<{width-4}}', f'{"":<1}{"_"*(width-2):<{width-4}}'
        if isinstance(_attr, str): 
            offset = len(_attr)
            if offset<4: 
                while offset!=4: offset+=1
            print(f'{top}\n{"":<1}|{_center(" "*(width-offset-2), _attr):<{width-4+len(Fore.GREEN)+len(Fore.RESET)}}|'); _index+=2
            for _ in range(height-_default+_index-_last): print(f'{"":<1}|{" "*(width-offset-2):<{width-4}}|') #-6 -> default; _index -> custom lines before autofill; -2 -> (-3 top in list instance),/ bottom & copyright(+maybe settings)
        elif isinstance(_attr, list):
            offsets={}
            for _k, _v in enumerate(_attr): 
                offsets[f'offset[{_k}]']=len(_v)

            if bool(_centered):
                for _k, _v in offsets.items():
                    if offsets[_k]<4:
                        while offsets[_k]!=4: offsets[_k]+=1
            try:
                if len(offsets)==len(_attr):
                    print(top); print(f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|')
                    for _k, offset in enumerate(offsets.values()):
                        if bool(_centered): print(f'{"":<1}|{_center(" "*(width-offset-2), _attr[_k]):<{width-4}}|'); _index+=1
                        else: print(f'{"":<1}|{"":<2}{_attr[_k]:<{width-6}}|'); _index+=1
                    for _ in range(height-_default-_index-_last): print(f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|')
                else: raise InsufficientError
            except InsufficientError:
                print(f"InsufficientError: Indexes of offsets & _attributes don't match.")
    finally: print(bottom); _style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■   Chip Browser © 2022%')

'''
dict of each len(offset) so i can execute for each line ig
'''

# def display(
#     _attr:str or list,
#     _string:str or None,
#     _index:int = 0
#     ):
#     if isinstance(_attr, str):
#         print(f'{"":<1}|{_center(" "*(width-_wrap.offset-2), _string):<{width-4}}'); _index+=1

    #elif isinstance(_attr, list):


def _dimensions(_string) -> ...:#_load('Loading Assets...'):
    while bool(69>>420>>ord('F')>>ord('U')>>ord('N')>>ord('N')>>ord('Y')<<ord(_i) for _i in 'AXINOOBLOLXD'): #best very fanny while loop
        geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
        geometry.__init__(_size().columns, _size().lines)
        __width__, globals()['width'] = width, geometry.__dict__['width']
        __height__, globals()['height'] = height, geometry.__dict__['height']
        if width!=__width__ or height!=__height__: system('cls'); display(_attr=_string, _centered=False, **geometry.__dict__)
        else: del geometry; sleep(2.2250738585072014e-308)


def _keydetection(ascii:object) -> ...:
    while True:
        system('taskkill /f /im python.exe') if getwch()==ascii.CTRL_Q else None

'''
manually set a variable for detection derived from the characters dict; EX: chr(ascii.characters['key'])
'''

detection=Thread(target=_dimensions, args=(response,)); detection.start()
keydetection=Thread(target=_keydetection, args=(ASCII_TABLE,)); keydetection.start()