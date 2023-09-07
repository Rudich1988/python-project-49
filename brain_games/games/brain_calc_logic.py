from random import choice, randint

GAME_RULES = 'What is the result of the expression?'
MIN_NUMBER_FOR_COLCULATE = 0
MAX_NUMBER_FOR_COLCULATE = randint(0, 20)


def play_brain_calc():
    operators = ('+', '-', '*')
    operand_1 = randint(MIN_NUMBER_FOR_COLCULATE, MAX_NUMBER_FOR_COLCULATE)
    operand_2 = randint(0, 20)
    action = choice(operators)
    question = f'{operand_1} {action} {operand_2}'
    if action == '*':
        result = operand_1 * operand_2
    elif action == '+':
        result = operand_1 + operand_2
    else:
        result = operand_1 - operand_2
    correct_answer = result
    return (GAME_RULES, question, correct_answer)
