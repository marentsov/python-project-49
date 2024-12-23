import math
from random import randint
from brain_games.game_engine import play



def generate_game():

    random_num_1 = randint(0, 100)
    random_num_2 = randint(0, 100)

    question = f'{random_num_1} {random_num_2}'

    result = math.gcd(random_num_1, random_num_2)

    return question, str(result)


def main():
    RULES = 'Find the greatest common divisor of given numbers.'
    play(generate_game, RULES)



if __name__ == '__main__':
    main()
