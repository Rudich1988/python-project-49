from brain_games.games.engine import engine, MAX_ROUND_QUANTITY
from random import randint


def make_res_list():
    long_list = randint(5, 10)
    step = randint(1, 20)
    res_lst = []
    start = randint(1, 100)
    for index in range(long_list):
        element = start + index * step
        res_lst.append(element)
    return res_lst


def play_brain_progression():
    game_rules = 'What number is missing in the progression?'
    correct_answers = []
    questions = []
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        res_lst = make_res_list()
        random_index = randint(0, len(res_lst) - 1)
        correct_answer = res_lst[random_index]
        res_lst[random_index] = '..'
        str_res_list = [str(res_lst[k]) for k in range(len(res_lst))]
        question = ' '.join(str_res_list)
        correct_answers.append(correct_answer)
        questions.append(question)
        current_round += 1
    return engine(game_rules, questions, correct_answers)
