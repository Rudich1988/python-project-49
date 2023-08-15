from brain_games.games.engine import engine, ROUND_NUMBER
from random import randint


def brain_even_logic():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    answer_correct = []
    questions = []
    for i in range(ROUND_NUMBER):
        question = randint(0, 1000)
        if question % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        answer_correct.append(result)
        questions.append(question)
    return engine(game_rules, questions, answer_correct)
