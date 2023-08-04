#!/usr/bin/env python3
from random import randint
from brain_games.games.all_games import engine
from brain_games.cli import welcome_user


def gcd():
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 0
    for i in range(3):
        num_1 = str(randint(1,100))
        num_2 = str(randint(1, 100))
        string = num_1 + ' ' + num_2
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
    gcd()
