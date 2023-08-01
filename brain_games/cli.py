import prompt


def welcome_user():
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')


if __name__ == '__main__':
    welcome_user()
