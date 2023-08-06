from brain_games.games.all_games import engine, ROUND_NUMBER
from random import randint


def brain_gcd_logic():
    print('Welcome to the Brain Games!')
    game_rules = 'Find the greatest common divisor of given numbers.'
    answer_correct = []
    questions = []
    for i in range(ROUND_NUMBER):
        numb_1 = randint(1, 100)
        numb_2 = randint(1, 100)
        question = f'{numb_1} {numb_2}'
        n = min([numb_1, numb_2])
        while n > 0:
            if numb_1 % n == 0 and numb_2 % n == 0:
                result = n
                break
            else:
                n -= 1
        questions.append(question)
        answer_correct.append(result)
    return engine(game_rules, questions, answer_correct)
