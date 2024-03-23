from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
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
    if len(divisors) == 2:
        return True
    return False


def get_game_data():
    number = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    prime_number = is_prime(number)
    if prime_number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
