from random import randint
from brain_games.game_engine import play

RULES = 'What number is missing in the progression?'


def generate_game():

    random_start = randint(0, 10)
    random_step = randint(2, 5)
    random_lenght = randint(5, 10)
    random_index = randint(0, random_lenght - 1)

    progression = [random_start + random_step * i for i in range(random_lenght)]
    result = progression[random_index]
    progression[random_index] = '..'
    question = " ".join(map(str, progression))

    return question, str(result)


def main():
    RULES = 'What number is missing in the progression?'
    play(generate_game, RULES)

if __name__ == '__main__':
    main()
