from random import randint

GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER_FOR_QUESTION = 1
MAX_NUMBER_FOR_QUESTION = 100


def is_prime(number):
    divisors = []
    if number >= 2:
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                divisors.append(divisor)
    else:
        divisors = []
    return divisors


def play_brain_prime():
    number = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    number_divisors = is_prime(number)
    question = number
    if len(number_divisors) == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return (GAME_RULES, question, correct_answer)
