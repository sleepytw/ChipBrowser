'''
ANSI DETAILED DESCRIPTION -> 
        ext/ANSI.md;
'''

import os
os.system("")


class IlliterateMonkey(Exception): pass


CSI = '\033[' # Control Sequence Introducer: sequence starting with ESC [ or CSI (\x9B)


def _transf(code): return CSI + str(code) + 'm'


class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value=getattr(self, name)
                setattr(self, name, _transf(value))


class AnsiEffect:
    BOLD            = u"\u001b[1m"
    UNDERLINE       = u"\u001b[0m\u001b[4m"
    REVERSED        = u"\u001b[0m\u001b[7m"
    RESET           = u"\u001b[0m"


class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107


class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0


Effect = AnsiEffect()
Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()

def start_index(_string: str): return [_i for (_i, _) in enumerate(_string) if _=='&']
def end_index(_string: str): return [_i for (_i, _) in enumerate(_string) if _=='@']
def str_index(_string: str): return [_i for (_i, _) in enumerate(_string) if _=='%']

class Colorize:
    def beautify(self, _line: str) -> str:
        '''
        When using the multiline, u have to index the position for the next color
        example: &1hello&2world
        &1->hello {green}
        ->reset
        &2->world{red}
        '''

        _init=dict(zip(start_index(_line), end_index(_line))); colors={}
        _str=dict(zip(end_index(_line), str_index(_line))); _msg=str()

        for _k, _v in _init.items():
            try:
                if _line[_k+1:_v] in vars(Fore): colors.update({f'Fore.{_line[_k+1:_v]}': ''})
                elif _line[_k+1:_v] in vars(Back): colors.update({f'Back.{_line[_k+1:_v]}': ''})
                elif _line[_k+1:_v] in vars(Style): colors.update({f'Style.{_line[_k+1:_v]}': ''})
                else: raise IlliterateMonkey
            except IlliterateMonkey:
                print('Non-existant given value by your dumbass in the database.')

        __operand__=list(zip(colors, [f'"""{_line[_p+1:_i]}"""' for _p, _i in _str.items()]))
        _msg='+'.join(['+'.join(_cache) for _cache in __operand__])
        return exec(f"print(%s)" % (_msg))
        

_style=Colorize()
#_style.beautify('&BLACK@■%&RED@■%&GREEN@■%&YELLOW@■%&BLUE@■%&MAGENTA@%■&CYAN@■%&WHITE@■%&RESET@■%')