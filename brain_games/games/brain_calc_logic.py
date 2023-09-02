from brain_games.games.engine import engine, MAX_ROUND_QUANTITY
from random import randint, choice


def play_brain_calc():
    game_rules = 'What is the result of the expression?'
    answer_correct = []
    questions = []
    operands = ['+', '-', '*']
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        numb_1 = randint(0, 20)
        numb_2 = randint(1, 20)
        action = choice(operands)
        question = f'{numb_1} {action} {numb_2}'
        if action == '*':
            result = numb_1 * numb_2
        elif action == '+':
            result = numb_1 + numb_2
        else:
            result = numb_1 - numb_2
        questions.append(question)
        answer_correct.append(result)
        current_round += 1
    return engine(game_rules, questions, answer_correct)
