from pyautogui import size
from os import system, get_terminal_size as _size
from threading import Thread

class wm_geometry:
    def __init__(self, width, height):
        self.width, self.height = width, height #width and height in columns & rows

'''
could be used dynamically by initializing a __new__ class everytime the scale changes(dimensions)
works by offesting a value from globals() by deriving the scale values from the geometry class
i fear it might be a little slow tho xd will see cba
'''

def _center(format:str, string:str):
    center=int(len(format)/2)   
    return format[:center]+string+format[center+len(string):] 

def _wrap(string, **kwargs):
    try:
        width, height = kwargs['width'], kwargs['height']
        print(f'{"":<1}{"-"*(width-2):<{width-4}}\n{"":<1}|{_center(" "*(width-9), string):<{width-4}}|')
        for _ in range(height-4): print(f'{"":<1}|{" "*(width-9):<{width-4}}|')
    finally: print(f'{"":<1}{"-"*(width-2):<{width-4}}')

def _detect() -> ...:
    geometry=wm_geometry(_size().columns, _size().lines)
    geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
    geometry.__init__(_size().columns, _size().lines)
    width=geometry.__dict__['width']; height=geometry.__dict__['height']
    _wrap('TITLE', **geometry.__dict__)
    while True:
        geometry=wm_geometry(_size().columns, _size().lines)
        geometry=object.__new__(wm_geometry, _size().columns, _size().lines)
        geometry.__init__(_size().columns, _size().lines)
        __width__, width = width, geometry.__dict__['width']
        __height__, height = height, geometry.__dict__['height']
        if width!=__width__ or height!=__height__:
            system('cls')
            _wrap('TITLE', **geometry.__dict__)

detection=Thread(target=_detect); detection.start()