import math
import time
import os

from ..ChipEngine.random_generator import RANDOM as random

#SEED BASE (TAKAHIRO) -> $3148075014752687238943813 \
# 672356493854626349123837249188635215849876355629543767827420021560257490570296502570572950257602


class OFFSETS(object):

    def __init__(self, capacity, config, primes) -> str: ...

    def GENERATE_PRIMES(self) -> int: 
        return [
            num for num in range(math.abs(self.capacity/2), math.abs(self.capacity*2)+1) for x in range(2, num) if (num % x) == 0 if num > 1
            ]

    def GENERATE_SEED() -> int:
        with open('seed.pxd', 'w', encoding='utf8') as seed_file:
            seed_file.write('')