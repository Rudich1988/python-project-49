from brain_games.games.engine import engine, ROUND_NUMBER
from random import randint, choice


def brain_calc_logic():
    game_rules = 'What is the result of the expression?'
    answer_correct = []
    questions = []
    lst = ['+', '-', '*']
    for i in range(ROUND_NUMBER):
        numb_1 = randint(0, 20)
        numb_2 = randint(1, 20)
        action = choice(lst)
        question = f'{numb_1} {action} {numb_2}'
        if action == '*':
            result = numb_1 * numb_2
        elif action == '+':
            result = numb_1 + numb_2
        else:
            result = numb_1 - numb_2
        questions.append(question)
        answer_correct.append(result)
    return engine(game_rules, questions, answer_correct)
