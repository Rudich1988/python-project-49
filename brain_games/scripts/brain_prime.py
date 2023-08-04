from random import randint
from brain_games.games.all_games import engine
from brain_games.cli import welcome_user


def prime():
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for i in range(3):
        numb = str(randint(1, 100))
        result = engine(numb)
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
    prime()