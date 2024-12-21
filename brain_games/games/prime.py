from random import randint
import math
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def num_prime(num):
    if num <= 1:
        return False
    num_sqrt = int(math.sqrt(num))
    num_divisors = range(2, (num_sqrt + 1))
    for item in num_divisors:
        if num % item == 0:
            return False

    return True


def generate_game():
    question = randint(0, 100)
    num = question
    if num_prime(num):
        result = 'yes'
    else:
        result = 'no'

    return question, result



