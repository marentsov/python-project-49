from random import choice, randint

from brain_games.game_engine import play


def generate_game():

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


def main():
    RULES = 'What is the result of the expression?'
    play(generate_game, RULES)


if __name__ == '__main__':
    main()




