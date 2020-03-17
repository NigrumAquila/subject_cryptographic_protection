from math import sqrt
from random import randint

def is_prime(number: int) -> bool:
    if (number % 2 == 0):
        return False

    dividend = sqrt(number)
    divider = 3
    while divider <= dividend:
        if number % divider == 0:
            return False
        divider += 2

    return True

def prime_generator(noLess: int = 300, noMore: int = 500) -> int:
    number = randint(noLess, noMore)
    while True:
        number += 1
        if is_prime(number):
            return number