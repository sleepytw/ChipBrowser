import json, os, importlib
class EmptyException(Exception): pass

def validate(file):
    """ Check if file is empty by confirming if its size is 0 bytes"""
    return os.path.exists(f'{file}.py') and os.stat(f'{file}.py').st_size == 0

def modules(_c=None): #_c ~ cache
    data=json.load(open('data.json')); _c=list();
    try:
        for _m in data['modules']:
            if validate(_m): _c.append(_m);
            else: globals()[_m] = importlib.import_module(_m); #-> also make it list all functions and desc or wahtever the fuck
        if len(_c)!=0: raise EmptyException
        else: return None
    except EmptyException:
        print(f"""Unimported module/s:\n{['%s' % _i for _i in _c]}""")

