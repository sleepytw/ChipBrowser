from os import system, path, get_terminal_size as _size
from abc import abstractmethod
import importlib
import platform
import asyncio
import ctypes
import re
import sys
import os

import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from msvcrt import getwch, putwch
import shutil
import numpy as np

from functools import lru_cache, cache
from threading import Thread as Process
from time import perf_counter, sleep #internal cpu clock

from color_interpreter import Effect, Fore, Back, Style, _style
from requestslib3 import get, post
from __init__ import basemethod

path = os.path.dirname(os.path.abspath(__file__)) #path to file
importlib.import_module('')


class geometry_init:

    def __init__(self, width, height):
        self.width, self.height = (
            width, height
            )  # width & height in columns & rows


geometry    =   geometry_init(_size().columns, _size().lines)
width       =   geometry. __dict__ ["width"]
height      =   geometry. __dict__ ["height"]

EasterEgg   =   True

__ASSETS__  =   [
    'asyncio.run(_title("Chip Browser"))',
    "asyncio.run(_icon())",
    #"_screen.set(1920, 1080)",
    "_screen.fullscreen()"
]


def rainbow_credits(text: str):
    while True:
        output = f'{text}\r' # '\t'*int(shutil.get_terminal_size()[0])
        color_options = [color for color in vars(Fore) if color not in ["LIGHTBLACK_EX", "LIGHTWHITE_EX", "BLACK", "WHITE", "RESET"]]
        output = getattr(Fore, RANDOM.urandom(color_options).upper()) + output #f'{"":<15}'

        print("\033[1;1H"+output+"\033[1;1H") # '\n'*int(shutil.get_terminal_size()[1])
        sleep(0.04)


class InsufficientError(Exception):
    ...


async def _title(attr: str = None) -> ...:
    return ctypes.windll.kernel32.SetConsoleTitleW("Chip Browser")


async def _icon(arg: None = None) -> ...:
    return None


def _transf(code):
    return chr(
        code
    )  # manually set a variable for detection derived from the characters dict; EX: chr(ascii.characters['key'])


class conn_establish(object):
    # Sadly https sites encrypt data in a certain way, as to which you cant read shit from it unless ur sending an https request aswell
    # Therefore if the response is scuffed/ straight up gives an error for unicodedecode, just change the proxy to 127.0.0.1 which would resolve the issue
    # One caveat is that ur no longer hidden in terms of ur ip so um take ur chances ig :P
    
    @classmethod
    def http(
        self, 
        url   : str, 
        port  : int,
        path  : str, 
        proxy : str
    ) -> list:

        global _url, _port, _path, _proxy, response
        _url, _port, _path, _proxy, response = url, port, path, proxy, []
        init_response = re.split("\r\n", bytes(get(
                                                    (url, port), path, (proxy, port)),
                                                    encoding='utf-8').decode())
        for _i, _ in enumerate(init_response):
            for _j in init_response[_i].split("\n"):
                response.append(_j.strip())
        return response

    @abstractmethod
    def http_to_https(
        _: ...) -> ...:
        return  # integrated into requestslib3 already


conn_establish.http(
                    url   = "httpbin.org",
                    port  = 80,
                    path  = "/ip",
                    proxy = "103.117.192.14"
                )


class LOAD_ASSETS(object):

    @classmethod
    def progress_bar(cls, progress, total, asset):
        percent = 100 * (progress / float(total))
        bar = "#" * int(percent) + "-" * (100 - int(percent))
        print(Fore.YELLOW + f"\r|{bar}| {percent:.2f}%", end="\r")
        if progress == total:
            print(Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")
            print(Fore.CYAN + "\n\n[LOADED ASSETS]" + Fore.RESET)
            for _i, _x in enumerate(__ASSETS__):
                print(Fore.WHITE + f"-> {_x}")
            print(Fore.RESET + "")

    @classmethod
    def search_bar(cls, text: str = "-> "):
        for x in text:
            putwch(x)
        string = ""
        while True:
            symbol = getwch()
            if symbol == "\n" or symbol == "\r":
                break
            print(symbol, end="", flush=True)
            string += symbol
        return string


def Background(object: None):
    global COLUMNS, ROWS
    snowflakes = {}


    def get_terminal_size():
        return shutil.get_terminal_size()


    COLUMNS, ROWS = get_terminal_size()
    ROWS-=3


    def get_random_flake():
        try:
            flake = RANDOM.urandom([' *',
                                   u' ❄' , 
                                   u' ❅'  ,
                                   u' ❆'  ])

            if flake is not None:
                return flake
            else:
                raise UnicodeError
        except UnicodeError:
            pass

        return " *"

    current_rows = {}


    def print_col(col, color):
        output = "\033[%s;%sH%s" % (snowflakes[col][0], col, snowflakes[col][1])
        if color:
            if color == "rainbow":
                color_options = [color for color in vars(Fore) if color not in ["LIGHTBLACK_EX", "LIGHTWHITE_EX", "BLACK", "WHITE", "RESET"]]
                output = getattr(Fore, RANDOM.urandom(color_options).upper()) + output
            else:
                output = getattr(Fore, color.upper())

        print(output)

        # reset the cursor
        print("\033[1;1H")


    def move_flake(col, stack, particle, color):
        # Rows is the max amount of rows on the screen,
        # so settings the column to the rows count means
        # putting it at the bottom of the screen

        if stack == "pile":
            if col not in current_rows:
                current_rows[col] = ROWS

            current_row = current_rows[col]

            # The current column has reached the top of
            # the screen, lets reset it so it drops the
            # pile back
            if current_row == 1:
                current_row = ROWS
                current_rows[col] = current_row

            # If next row is the end, lets just move the rows up by one
            if snowflakes[col][0] + 1 == current_row:
                current_rows[col] -= 1
        else:
            current_row = ROWS

        # If next row is the end, lets start a new snow flake
        if snowflakes[col][0] + 1 == current_row:
            char = particle
            if not particle:
                char = get_random_flake()
            snowflakes[col] = [1, char]
            print_col(col, color)
        else:
            # erase the flake in current location
            print("\033[%s;%sH  " % (snowflakes[col][0], col))
            # move down by one
            snowflakes[col][0] += 1
            print_col(col, color)


    def random_printer(speed, particle, stack, color):
        system('cls')

        while True:
            col = RANDOM.urandom(range(1, int(COLUMNS)))

            # Don't print snowflakes right next to each other, since
            # unicode flakes take 2 spaces
            if col in range(0, 5) or col in range(COLUMNS-5, COLUMNS):
                continue


            # its already on the screen, move it
            if col in snowflakes.keys():
                move_flake(col, stack, particle, color)
            else:
                # otherwise put it on the screen
                flake = particle if particle else get_random_flake()
                snowflakes[col] = [1, flake]
                print_col(col, color)

            # key any flakes on the screen moving
            for flake in snowflakes.keys():
                move_flake(flake, stack, particle, color)

            final_speed = 1.0 / speed

            try:
                sleep(final_speed)
            except KeyboardInterrupt:
                system('cls')
                sys.exit(0)


    def _main(speed=14, stack=None, particle=None, color=None):
        # Print all the flakes
        # for flake in range(0x2740, 0x2749):
        #   print(f"{flake}: {chr(flake)}")
        random_printer(speed, particle, stack, color)
    
    _main(color='rainbow')


class _screen(object):
    @classmethod
    def set(
        cls, 
        width  : None = None, 
        height : None = None, 
        depth  : int  = 32
    ):

        """
        Set the primary display to the specified mode
        """

        if sys.platform == "win32":
            cls._win32_set(width, height, depth)
        elif sys.platform.startswith("linux"):
            cls._linux_set(width, height, depth)

    @classmethod
    def fullscreen(cls):
        kernel32 = ctypes.WinDLL("kernel32")
        user32 = ctypes.WinDLL("user32")

        SW_MAXIMIZE = 3

        hWnd = kernel32.GetConsoleWindow()
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

    @staticmethod
    def _win32_get():
        """
        Get the primary windows display width and height
        """

        user32 = ctypes.windll.user32
        screensize = (
            user32.GetSystemMetrics(0),
            user32.GetSystemMetrics(1),
        )
        return screensize

    @staticmethod
    def _win32_set(
        width  : None = None, 
        height : None = None, 
        depth  : int  = 32
    ):

        """
        Set the primary windows display to the specified mode
        """
        import win32api

        if width and height:
            if not depth:
                depth = 32

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth, mode.PelsHeight, mode.BitsPerPel = width, height, depth

            win32api.ChangeDisplaySettings(mode, 0)

        else:
            win32api.ChangeDisplaySettings(None, 0)

    @staticmethod
    def _win32_set_default():
        """
        Reset the primary windows display to the default mode
        """

        user32 = ctypes.windll.user32
        # set screen size
        user32.ChangeDisplaySettingsW(None, 0)


class _LIMITER:

    def __init__(self, arg: int):
        self.arg = arg

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                for _ in range(self.arg):
                    return func(*args, **kwargs)

        wrapper.has_run = False
        return wrapper


class Iterators(object):
    # Doesnt save current index into memory of current iteration
    # Example: for _k in iterable: print(Iterators.__next__(Iterators.__iter__(iterable)))
    # Example 2: for _i in Iterators.__gen__(iterable): print(_i)

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current

    def __gen__(self):
        for _i in range(self.n):
            yield _i


class _DECIPHER(object):

    def __init__(self):
        for char in dir(self):
            if not char.startswith("_") & char == "characters":
                value = getattr(self, char)
                setattr(self, char, _transf(value))


"""
_DECIPHER (AUTO):
-exclude all list/dicts/etc unless converted
-initiate the object -> ex: ascii=ASCII_TABLE(); otherwise u can use chr(var) when converting manually
"""


class ASCII_TABLE(_DECIPHER):
    
    characters = {}
    for _, _v in enumerate("!\"#$%&'()*+,-./0123456789:;<=>?@ \
                            ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_` \
                            abcdefghijklmnopqrstuvwxyz{|}~"):
        characters[_v] = ord(_v)

    CTRL_Q = chr(
        17
    )  # kill switch (exit) manual: chr(17) -> a little dangerous cuz threading is lil hard on the memory but python makes sure it bins everythign so we fine :D


def _center(
    format : str,
    string : str
):

    center = int(len(format) / 2)
    return (
        format[:center + 6] + string + format[center + len(string):]
    )  # color -> f'{Fore.COLOR+string+Fore.RESET}'


def display_single(
    _attr         : str,
    _offset_multi : int   or None,
    _centered     : bool,
    _width        : int   or None,
    _height       : int   or None,
    **kwargs      : dict  or None,
):

    if kwargs != None and (_width and _height == None):
        width, height = kwargs["width"], kwargs["height"]
    else:
        width, height = _width, _height

    if _offset_multi is None:
        offset = len(_attr)
        if offset < 4:
            while offset != 4:
                offset += 1

    elif isinstance(_offset_multi, int):
        offset = _offset_multi
        if offset < 4:
            while offset != 4:
                offset += 1

    if _attr == "SPACE":
        print(f'{"":<1}|{" "*(width-offset-2):<{width-4}}|')

    if isinstance(_centered, bool) and _centered is False and _attr != "SPACE":
        print(f'{"":<1}|{"":<2}{_attr:<{width-6}}|')

    elif isinstance(_centered,
                    bool) and _centered is True and _attr != "SPACE":
        print(
            f'{"":<1}|{_center(" "*(width-offset-2), _attr):<{width-4+len(Fore.CYAN)+(len(Effect.BOLD)+len(Effect.UNDERLINE)+len(Effect.RESET)) if Effect.BOLD and Effect.UNDERLINE and Effect.RESET in _attr else 0}}|'
        )


def display(
        _attr     : str or list,  # *list -> **strings
        _centered : bool,  # y/n center
        _index    : int = 0,  # each message
        _default  : int = 5,  # default console centering
        _last     : int = 3,  # last & start
        **kwargs  : dict,  # resolution info
):
    system("cls")
    width, height = kwargs["width"], kwargs["height"]
    top, bottom = (
        f'{"":<1}{"_"*(width-2):<{width-4}}',
        f'{"":<1}{"_"*(width-2):<{width-4}}',
    )

    '''
    append each line to list and maybe parse it, after maybe just maybe yk do the same as the rainbow shit again so i cna print it each iteration
    without the snow covering the letters xD
    '''
    
    if bool(EasterEgg):
        print('\n'+Fore.RESET+top)
    else:
        print(top)
    _index += 1

    try:
        if isinstance(_attr, str):
            offset = len(_attr)
            if offset < 4:
                while offset != 4:
                    offset += 1
            print(
                f'{"":<1}|{_center(" "*(width-offset-2), _attr):<{width-4}}|')
            _index += 1  # color -> :<{width-4+len(Fore.COLOR)+len(Fore.RESET)}
            for _ in range(height - _default + _index - _last):
                print(
                    f'{"":<1}|{" "*(width-offset-2):<{width-4}}|'
                )  # -6 -> default; _index -> custom lines before autofill; -2 -> (-3 top in list instance),/ bottom & copyright(+maybe settings)
        elif isinstance(_attr, list):
            offsets = {}
            for _k, _v in enumerate(_attr):
                offsets[f"offset[{_k}]"] = len(_v)

            if bool(_centered):
                for _k, _v in offsets.items():
                    if offsets[_k] < 4:
                        while offsets[_k] != 4:
                            offsets[_k] += 1
            try:
                if len(offsets) == len(_attr):
                    print(
                        f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|'
                    )
                    for _x in [
                            Effect.UNDERLINE + Effect.BOLD + Fore.CYAN +
                            f"WEBSITE: {_url}{_path} ~ PORT: {_port} ~ PROXY: {_proxy}"
                            + Effect.RESET,
                            "SPACE",
                    ]:
                        display_single(
                            _attr         = _x,
                            _centered     = True,
                            _offset_multi = None,
                            _width        = width,
                            _height       = height,
                            kwargs        = None,
                        )
                        _index += 1
                    for _k, offset in enumerate(offsets.values()):
                        if bool(_centered):
                            print(
                                f'{"":<1}|{_center(" "*(width-offset-2), _attr[_k]):<{width-4}}|'
                            )
                            _index += 1
                        else:
                            print(f'{"":<1}|{"":<2}{_attr[_k]:<{width-6}}|')
                            _index += 1
                    for _ in range(height - _default - _index - _last + 2):
                        print(
                            f'{"":<1}|{" "*(width-max(offsets.values())-2):<{width-4}}|'
                        )
                else:
                    raise InsufficientError
            except InsufficientError:
                print(
                    f"InsufficientError: Indexes of offsets & _attributes don't match."
                )
    finally:
        print(bottom)
        _style.beautify(
            "&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■   Chip Browser © 2022%"
        )


# backround->(u"\u001b[48;5;")
@_LIMITER(arg=1)
def _load(**kwargs) -> str:
    width = kwargs["width"]
    height = kwargs["height"]
    for _i, _x in enumerate(__ASSETS__):
        exec(_x)
        LOAD_ASSETS.progress_bar(_i + 1, len(__ASSETS__), _x)
    sleep(1)
    for _ in range(10):
        for i in range(0, 16):
            for j in range(0, 30):
                code = str(i * 16 + j)
                sys.stdout.write("\u001b[38;5;" + code + "m " + code.ljust(4))
    print("\u001b[0m")
    system("cls")


#TODO: getattr/setattr to print the text on the screen so that it doesnt get fucked by the snowflakes and shit xD


def main(_string) -> _load(
        **geometry.__dict__
    ):
    while True:
        global width, height
        geometry = object.__new__(geometry_init, _size().columns, _size().lines)
        geometry. __init__ (_size().columns, _size().lines)
        __width__  ,  globals()["width"]  = width,    geometry. __dict__ ["width"]
        __height__ ,  globals()["height"] = height,   geometry. __dict__ ["height"]
        if width != __width__ or height != __height__:
            system("cls")
            display(
                _attr     = _string,
                _centered = False, 
                **geometry.__dict__
            )
        else:
            del geometry
            sleep(2.2250738585072014e-308) #shortest time u could pause for, just making sure the script doesnt stall


def _keydetection(ascii: object) -> ...:
    while True:
        system(
            "taskkill /f /im python.exe") if getwch() == ascii.CTRL_Q else None
        ... if getwch() == chr(ascii.characters["/"]) else None
        # refresh upon pressing a button kinda hard tho, hvae to reiterate all vars from recepient func


Process(target=RANDOM.timer).start() #cpu calibration
Process(target=main, args=(response,)).start() #main
Process(target=_keydetection, args=(ASCII_TABLE,)).start() #keydetection


if bool(EasterEgg):
    Process(target=rainbow_credits, args=('-> by sleepytw xD',)).start() #rainbow credits
    Background()