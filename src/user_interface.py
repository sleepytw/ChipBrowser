from __future__ import print_function
from os import system, path, get_terminal_size as _size
import re
import sys

from pyautogui import size
from msvcrt import getwch

from functools import lru_cache, cache
from threading import Thread
from time import sleep

from color_interpreter import Fore, Back, Style, _style
from requestslib3 import get, post

class InsufficientError(Exception): ...

url='httpbin.org'; port=80; _path='ip'
response=re.split('\r\n',get((url, port), _path, ('103.117.192.14', 80)))
if url=='httpbin.org' and (_path=='ip' or _path=='get'):
    for _i in response[-1].split('\n'): response.append(_i.strip())
    if _path=='ip': del response[-5]
    elif _path=='get':
        del response[-16]


def _title(attr:str)->...: return system(f'TITLE {attr}')
def _icon(arg=None)->...: return None
def _transf(code): return chr(code) #manually set a variable for detection derived from the characters dict; EX: chr(ascii.characters['key'])

__ASSETS__=['_title("Chip Browser")', '_icon()', '_screen.set(1920, 1080)', 'system(f"mode {width+1}, {height+1}")']

class LOAD_ASSETS(object):
    numbers=[x*5 for x in range(2000, 3000)]
    @classmethod
    def progress_bar(cls, progress, total, asset):
        percent=100*(progress/float(total))
        bar='#'*int(percent)+'-'*(100-int(percent))
        print(Fore.YELLOW+f'\r|{bar}| {percent:.2f}%', end='\r')
        if progress==total:
            print(Fore.GREEN+f'\r|{bar}| {percent:.2f}%', end='\r')
            print(Fore.CYAN+'\n\n[LOADED ASSETS]'+Fore.RESET)
            for _i, _x in enumerate(__ASSETS__): print(Fore.WHITE+f'-> {_x}')
            print(Fore.RESET+'')


class wm_geometry:
    def __init__(self, width, height): self.width, self.height = width, height #width & height in columns & rows

geometry=wm_geometry(_size().columns, _size().lines)
width=geometry.__dict__['width']; height=geometry.__dict__['height']

class _screen(object):
    @classmethod
    def set(cls, width=None, height=None, depth=32):
        '''
        Set the primary display to the specified mode
        '''

        if sys.platform == 'win32': cls._win32_set(width, height, depth)
        elif sys.platform.startswith('linux'): cls._linux_set(width, height, depth)        

    @staticmethod
    def _win32_get():
        '''
        Get the primary windows display width and height
        '''
        import ctypes
        user32 = ctypes.windll.user32
        screensize = (
            user32.GetSystemMetrics(0), 
            user32.GetSystemMetrics(1),
            )
        return screensize

    @staticmethod
    def _win32_set(width=None, height=None, depth=32):
        '''
        Set the primary windows display to the specified mode
        '''
        import win32api
        if width and height:
            if not depth: depth = 32

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth, mode.PelsHeight, mode.BitsPerPel = width, height, depth

            win32api.ChangeDisplaySettings(mode, 0)

        else: win32api.ChangeDisplaySettings(None, 0)

    @staticmethod
    def _win32_set_default():
        '''
        Reset the primary windows display to the default mode
        '''
        
        import ctypes
        user32 = ctypes.windll.user32
        # set screen size
        user32.ChangeDisplaySettingsW(None, 0)


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

def _center(format:str, string:str):
    center=int(len(format)/2)
    return format[:center]+string+format[center+len(string):] # color -> f'{Fore.COLOR+string+Fore.RESET}'

def display_single(
    _attr:str, 
    _offset_multi:int or None,
    _centered:bool, 
    _width:int or None,
    _height:int or None,
    **kwargs:dict or None
    ):

    if kwargs!=None and (_width and _height == None): width, height = kwargs['width'], kwargs['height']
    else: width, height = _width, _height

    if _offset_multi is None:
        offset = len(_attr)
        if offset<4: 
            while offset!=4: offset+=1

    elif isinstance(_offset_multi, int):
        offset=_offset_multi
        if offset<4: 
            while offset!=4: offset+=1

    if _attr=='SPACE':
        print(f'{"":<1}|{" "*(width-offset-2):<{width-4}}|')

    if isinstance(_centered, bool) and _centered is False and _attr!='SPACE':
        print(f'{"":<1}|{"":<2}{_attr:<{width-6}}|')

    elif isinstance(_centered, bool) and _centered is True and _attr!='SPACE':
        print(f'{"":<1}|{_center(" "*(width-offset-2), _attr):<{width-4}}|')


def display(
    _attr:str or list, # *list -> **strings
    _centered:bool, # y/n center
    _index:int=0, #each message
    _default:int=6, # default console centering
    _last:int=3, #last & start
    **kwargs:dict #resolution info
    ):
    system('cls')
    width, height = kwargs['width'], kwargs['height']
    top, bottom = f'{"":<1}{"_"*(width-2):<{width-4}}', f'{"":<1}{"_"*(width-2):<{width-4}}'
    print(top); _index+=1
        
    try:
        if isinstance(_attr, str):
            offset = len(_attr)
            if offset<4: 
                while offset!=4: offset+=1
            print(f'{"":<1}|{_center(" "*(width-offset-2), _attr):<{width-4}}|'); _index+=1  # color -> :<{width-4+len(Fore.COLOR)+len(Fore.RESET)}
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
                    print(f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|')
                    for _i in [f'WEBSITE: {url}/{_path}, PORT: {port}', 'SPACE']: 
                        display_single(_attr=_i, _centered=True, _offset_multi=None, _width=width, _height=height, kwargs=None); _index+=1
                    for _k, offset in enumerate(offsets.values()):
                        if bool(_centered): print(f'{"":<1}|{_center(" "*(width-offset-2), _attr[_k]):<{width-4}}|'); _index+=1
                        else: print(f'{"":<1}|{"":<2}{_attr[_k]:<{width-6}}|'); _index+=1
                    for _ in range(height-_default-_index-_last+2): print(f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|')
                else: raise InsufficientError
            except InsufficientError:
                print(f"InsufficientError: Indexes of offsets & _attributes don't match.")
    finally: print(bottom); _style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■   Chip Browser © 2022%')


@_LIMITER(arg=1)
def _load(**kwargs):
    width=kwargs['width']; height=kwargs['height']
    for _i, _x in enumerate(__ASSETS__):
        exec(_x); LOAD_ASSETS.progress_bar(_i+1, len(__ASSETS__), _x); sleep(0.2)
    _style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■   Chip Browser © 2022%')
    sleep(2) 
    system('cls')


def _main(_string) -> _load(**geometry.__dict__):
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


main=Thread(target=_main, args=(response,)); main.start()
keydetection=Thread(target=_keydetection, args=(ASCII_TABLE,)); keydetection.start()