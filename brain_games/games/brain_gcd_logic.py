from brain_games.games.engine import engine, MAX_ROUND_QUANTITY
from random import randint


def play_brain_gcd():
    game_rules = 'Find the greatest common divisor of given numbers.'
    answer_correct = []
    questions = []
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        numb_1 = randint(1, 100)
        numb_2 = randint(1, 100)
        question = f'{numb_1} {numb_2}'
        divisor = min([numb_1, numb_2])
        while divisor > 0:
            if numb_1 % divisor == 0 and numb_2 % divisor == 0:
                greatest_divisor = divisor
                break
            else:
                divisor -= 1
        questions.append(question)
        answer_correct.append(greatest_divisor)
        current_round += 1
    return engine(game_rules, questions, answer_correct)
