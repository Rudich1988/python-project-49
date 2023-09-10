from random import randint

MIN_NUMBER_FOR_QUESTION = 1
MAX_NUMBER_FOR_QUESTION = 20
GAME_RULES = 'Find the greatest common divisor of given numbers.'


def find_greatest_divisor(number_1, number_2):
    divisor = min(number_1, number_2)
    while divisor > 0:
        if number_1 % divisor == 0 and number_2 % divisor == 0:
            break
        else:
            divisor -= 1
    return divisor


def get_game_data():
    number_1 = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    number_2 = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    question = f'{number_1} {number_2}'
    greatest_divisor = find_greatest_divisor(number_1, number_2)
    return question, greatest_divisor
