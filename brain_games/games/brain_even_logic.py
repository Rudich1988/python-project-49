from brain_games.games.engine import engine, MAX_ROUND_QUANTITY
from random import randint


def play_brain_even():
    game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    answer_correct = []
    questions = []
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        question = randint(0, 1000)
        if question % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        answer_correct.append(result)
        questions.append(question)
        current_round += 1
    return engine(game_rules, questions, answer_correct)
