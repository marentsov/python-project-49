from random import randint, choice
RULES = 'What is the result of the expression?'

def generate_game()

    random_num_1 = randint(0, 20)
    random_num_2 = randint(0, 20)
    random_symbol = choice('+-*')

    if random_symbol == '+':
        result = random_num_1 + random_num_2
    elif random_symbol == '-':
        result = random_num_1 - random_num_2
    elif random_symbol == '*':
        result = random_num_1 * random_num_2

    question = f'{random_num_1} {random_symbol} {random_num_2}'

    return question, str(result)







