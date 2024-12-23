from random import randint
from brain_games.game_engine import play



def generate_game():

    question = randint(1, 100)

    if question % 2 == 0:
        result = 'yes'
    elif question % 2 != 0:
        result = 'no'

    return question, result


def main():
    RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
    play(generate_game, RULES)



if __name__ == '__main__':
    main()

