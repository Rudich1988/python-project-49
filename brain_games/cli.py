import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    return username


if __name__ == '__main__':
    welcome_user()
