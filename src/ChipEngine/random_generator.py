from time import perf_counter, sleep #internal cpu clock
from threading import Thread as Process

import importlib
import numpy as np

from __init__ import basemethod


TRACK = []


class RANDOM(object):

    @classmethod
    def timer(cls, low: int = 0, high: int = 10, index: int = 0, seed=9223372036854775807, mult=16807, mod=(2**31) + 1):

        while True:
            cpu_time = perf_counter()
            index += (low+(high-low)*(11+cpu_time))
            TRACK.append((index + cpu_time) * (seed * mult + 1) % mod)
            sleep(2.2250738585072014e-308) #prevent overload
            TRACK.clear()
            index = 0

    @classmethod
    def algorithm(cls, low=0, high=1, mult=16807, mod=(2**31) + 1, seed=9223372036854775807, size=1):

        cpu_time = perf_counter()
        U = np.zeros(size)
        x = (seed * mult + 1) % mod
        U[0] = x / mod
        for i in range(1, size):
            x = (seed * mult + (i + cpu_time)) % mod
            U[i] = x / mod
        return U

    @classmethod
    def pseudo_uniform(cls, low=0, high=1, seed=9223372036854775807, size=1):

        return low + (high - low) * RANDOM.algorithm(seed=seed, size=size)

    @classmethod
    def urandom(cls, array: list, seed=9223372036854775807, size=1):
        #math could use some improvement its kinda late tho cba will see

        cpu_time = perf_counter()
        try:
            seed_local = int(10**9 * TRACK[0] * float(str(cpu_time - int(cpu_time))[0:]))
        except len(TRACK) == 0:
            seed_local = int(10**9 * float(str(cpu_time+1 - cpu_time+1)[0:]))
        idx = int(RANDOM.pseudo_uniform(low=0, high=len(array), seed=seed_local, size=1))
        return array[idx]

    @classmethod
    def shuffle(cls, array: list):
        for i, _ in enumerate(array):
            array[i] = array[RANDOM.urandom(array)]

        return array

    @basemethod
    def URANDOM_BLUEPRINT(cls):
        for _ in range(10):
            print(RANDOM.urandom(
                ['heads', 'tails']
                ), end=' ')

