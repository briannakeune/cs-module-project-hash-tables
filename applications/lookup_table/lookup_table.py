# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}


def slowfun(x, y):
    cache_key = f'{x},{y}'
    if cache_key not in cache:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[cache_key] = v

    return cache[cache_key]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x}, {y}: {slowfun(x, y)}')
