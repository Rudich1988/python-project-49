from random import randint

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER_FOR_QUESTION = 0
MAX_NUMBER_FOR_QUESTION = 1000


def play_brain_even():
    number = randint(MIN_NUMBER_FOR_QUESTION, MAX_NUMBER_FOR_QUESTION)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
