import prompt

ROUNDS = 3


def play(generate_game, RULES):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)

    for _ in range(ROUNDS):
        question, result = generate_game()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')

        if result == answer:
            print('Correct!')
        else:
            print(
                f'\"{answer}" is wrong answer ;(.'
                f' Correct answer was "{result}".')
            print(f"Let's try again, {name}!")
            break

    else:
        print(f'Congratulations, {name}!')



