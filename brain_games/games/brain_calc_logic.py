from random import choice, randint

GAME_RULES = 'What is the result of the expression?'
MIN_NUMBER_FOR_COLCULATE = 0
MAX_NUMBER_FOR_COLCULATE = 20


def play_brain_calc():
    operators = ('+', '-', '*')
    operand_1 = randint(MIN_NUMBER_FOR_COLCULATE, MAX_NUMBER_FOR_COLCULATE)
    operand_2 = randint(MIN_NUMBER_FOR_COLCULATE, MAX_NUMBER_FOR_COLCULATE)
    action = choice(operators)
    question = f'{operand_1} {action} {operand_2}'
    if action == '*':
        correct_answer = operand_1 * operand_2
    elif action == '+':
        correct_answer = operand_1 + operand_2
    else:
        correct_answer = operand_1 - operand_2
    return question, correct_answer
