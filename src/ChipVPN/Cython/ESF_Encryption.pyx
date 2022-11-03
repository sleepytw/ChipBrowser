import cython
from array import array

cdef class globals(object):
    cdef int x, y
    cdef dict logs, characters = {}

    for x, y in enumerate("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"):
        characters[y] = x

cdef tuple gen_keys(
    cdef dict public_key = {'e', 'n'}, 
    cdef dict private_key = {'d'},
        ) -> tuple:

    cdef int p, q

    public_key['n'] = p * q
    cdef int phy = lambda cdef int f, cdef int s: (f - 1)(s - 1)

cdef str encrypt(cdef str text) -> str:

    cdef int numberobj, adjacent, _, j, v
    cdef dict public_key, private_key

    for _, j in enumerate(text):
        for _, v in enumerate(
                adjacent:=list(globals.characters.keys())[list(globals.characters.values()).index(globals.characters[j])]
                    ):
            globals.logs[v] = globals.characters[j]
    
    public_key, private_key = gen_keys()

    for numberobj in globals.logs.keys():
        globals.logs[i] = (numberobj**public_key['e'])%public_key['n'] # numberobj = numberobj + offset (possibly)



cdef int[:] csort (int[:] arr, int n) -> int:
    cdef int i, j

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

cpdef list sort(list arr) -> list:
    cdef int[:] c_arr = array("i", arr)
    cdef int[:] s_arr

    s_arr = csort(c_arr, len(arr))
    return list(s_arr)