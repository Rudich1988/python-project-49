#!/usr/bin/env python3
from random import randint
import prompt


def main():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    lst = []
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        result = randint(-1000, 1000)
        if result not in lst:
            print(f'Question: {result}')
            answer = prompt.string('Your answer: ')
            if (answer == 'yes' and result % 2 == 0) or (answer == 'no' and
                                                         result % 2 != 0):
                print('Correct!')
                lst.append(result)
            else:
                if answer == 'no':
                    correct_answer = 'yes'
                else:
                    correct_answer = 'no'
                print(f"'{answer}' is wrong answer ;(.", end=' ')
                print(f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {username}!")
                break
        if len(lst) == 3:
            print(f'Congratulations, {username}')


if __name__ == '__main__':
    main()
