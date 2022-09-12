from glob import glob


class globals(object):
    logs       = {}
    characters = {}

    for x, y in enumerate("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"):
        characters[y] = x

def gen_keys() -> tuple: ...

def encrypt(text: str) -> str:
    for _, j in enumerate(text):
        for _, v in enumerate(adjacent:=list(globals.characters.keys())[list(globals.characters.values()).index(globals.characters[j])]):
            globals.logs[v] = globals.characters[j]
    
    public, private = gen_keys()

    for i in globals.logs.keys():
        ...
