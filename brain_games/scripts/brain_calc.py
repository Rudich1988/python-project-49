#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.all_games import engine
from random import randint, choice


def calc():
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print('What is the result of the expression?')
    count = 0
    lst = ['+', '-', '*']
    for i in range(3):
        num_1 = randint(0, 20)
        num_2 = randint(1, 20)
        action = choice(lst)
        string = f'{num_1} {action} {num_2}'
        result = engine(string)
        if result == 'Correct!':
            print(result)
            count += 1
        else:
            print(result)
            print(f"Let's try again, {hello}!")
            break
    if count == 3:
        print(f'Congratulations, {hello}!')


if __name__ == '__main__':
    calc()
