modules=['json', 'os']
import json, os
os.system("")

CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

_dynamics={_k: _v for _k, _v in globals().items() if not _k.startswith("__") and not _k in modules and not _k=='modules'}
with open('colors.json', 'w') as fp:
    _dump=json.dumps(dict((_i, eval(_i)) for _i in _dynamics), default=lambda o: o.__dict__, indent=2)
    fp.write(_dump)
    
class Colors:
    def __init__(self):
        self._exclude  = ...
        self.CEND      = '\33[0m'
        self.CBOLD     = '\33[1m'
        self.CITALIC   = '\33[3m'
        self.CURL      = '\33[4m'
        self.CBLINK    = '\33[5m'
        self.CBLINK2   = '\33[6m'
        self.CSELECTED = '\33[7m'

        self.CBLACK  = '\33[30m'
        self.CRED    = '\33[31m'
        self.CGREEN  = '\33[32m'
        self.CYELLOW = '\33[33m'
        self.CBLUE   = '\33[34m'
        self.CVIOLET = '\33[35m'
        self.CBEIGE  = '\33[36m'
        self.CWHITE  = '\33[37m'

        self.CBLACKBG  = '\33[40m'
        self.CREDBG    = '\33[41m'
        self.CGREENBG  = '\33[42m'
        self.CYELLOWBG = '\33[43m'
        self.CBLUEBG   = '\33[44m'
        self.CVIOLETBG = '\33[45m'
        self.CBEIGEBG  = '\33[46m'
        self.CWHITEBG  = '\33[47m'

        self.CGREY    = '\33[90m'
        self.CRED2    = '\33[91m'
        self.CGREEN2  = '\33[92m'
        self.CYELLOW2 = '\33[93m'
        self.CBLUE2   = '\33[94m'
        self.CVIOLET2 = '\33[95m'
        self.CBEIGE2  = '\33[96m'
        self.CWHITE2  = '\33[97m'

        self.CGREYBG    = '\33[100m'
        self.CREDBG2    = '\33[101m'
        self.CGREENBG2  = '\33[102m'
        self.CYELLOWBG2 = '\33[103m'
        self.CBLUEBG2   = '\33[104m'
        self.CVIOLETBG2 = '\33[105m'
        self.CBEIGEBG2  = '\33[106m'
        self.CWHITEBG2  = '\33[107m'

    def _dump(self, _line: str) -> ...:
        '''
        Essentially change the color of a sentence using pythons weird ascii syntax
        '''
        parse=_line.index('&')
        _colorBuffer=_line[:parse];
        #exec('%s = %s' % ())
        #print(globals())
        return ...

    def _multidump(self, _color: str, _line: str) -> ...:
        '''
        When using the multiline, u have to index the position for the next color
        example: &1hello&2world
        &1->hello {green}
        ->reset
        &2->world{red}
        '''

        return ...

style=Colors()
style._dump('style.CRED&color me uwu'); #print(style.CRED + 'color me uwu')

'''
_multidump will be built like _dumps' way of parsing the 2 strings
find & _dump
'''