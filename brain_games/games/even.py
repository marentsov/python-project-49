from random import randint
RULES = ('Answer "yes" if the number is even, otherwise answer "no".')


def generate_game():

    question = randint(1,100)

    if question % 2 == 0:
        result = 'yes'
    elif question % 2 != 0:
        result = 'no'

    return question, result



