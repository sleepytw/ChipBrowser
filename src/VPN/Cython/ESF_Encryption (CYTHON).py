import cython

cdef class globals(object):
    logs       = {}
    characters = {}

    for x, y in enumerate("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"):
        characters[y] = x

def gen_keys(
    public: dict = {'e', 'n'}, 
    private: dict = {'d'},
    p: int = 0,
    q: int = 0
        ) -> tuple:
    public['n'] = p * q
    phy: int = lambda p, q: (p - 1)(q - 1)

def encrypt(text: str) -> str:
    for _, j in enumerate(text):
        for _, v in enumerate(
                adjacent:=list(globals.characters.keys())[list(globals.characters.values()).index(globals.characters[j])]
                    ):
            globals.logs[v] = globals.characters[j]
    
    public, private = gen_keys()

    for numberobj in globals.logs.keys():
        globals.logs[i] = (numberobj**public['e'])%public['n'] # numberobj = numberobj + offset (possibly)
