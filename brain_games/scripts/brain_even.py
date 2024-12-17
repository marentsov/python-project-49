# игра - проверка на четность
# правильно ответить 3 раза

import random


counter = 0
while counter < 3:
    a = random.randint(0, 99)
    print(f'Question: {a}')
    b = input()
    if a % 2 == 0 and b == "yes":
        counter += 1
        if counter == 3:
            print('Congratulations')
            break
        print('Correct!')
    elif a % 2 != 0 and b == "no":
        counter += 1
        if counter == 3:
            print('Congratulations')
            break
        print('Correct!')
    else:
        print("Let's try again")




