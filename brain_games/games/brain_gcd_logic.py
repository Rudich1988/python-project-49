from random import randint

MIN_NUMBER_FOR_QUESTION = 1
MAX_NUMBER_FOR_QUESTION = 20


def play_brain_gcd():
    game_rules = 'Find the greatest common divisor of given numbers.'
    number_1 = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    number_2 = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    question = f'{number_1} {number_2}'
    divisor = min(number_1, number_2)
    while divisor > 0:
        if number_1 % divisor == 0 and number_2 % divisor == 0:
            greatest_divisor = divisor
            break
        else:
            divisor -= 1
    return (game_rules, question, greatest_divisor)
