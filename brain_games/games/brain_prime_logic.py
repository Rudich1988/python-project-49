from brain_games.games.engine import engine, MAX_ROUND_QUANTITY
from random import randint


def is_prime(numb):
    divisors = []
    if numb >= 2:
        for j in range(1, numb + 1):
            if numb % j == 0:
                divisors.append(j)
    else:
        divisors = []
    return divisors


def play_brain_prime():
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    answer_correct = []
    questions = []
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        numb = randint(1, 100)
        numb_divisors = is_prime(numb)
        if len(numb_divisors) == 2:
            result = 'yes'
        else:
            result = 'no'
        questions.append(numb)
        answer_correct.append(result)
        current_round += 1
    return engine(game_rules, questions, answer_correct)
