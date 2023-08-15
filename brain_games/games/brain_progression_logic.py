from brain_games.games.engine import engine, ROUND_NUMBER
from random import randint


def generation_result(arg):
    res = arg.split()
    for k in range(len(res) - 1):
        if res[k] != '..' and res[k + 1] != '..':
            step = int(res[k + 1]) - int(res[k])
            break
    index = res.index('..')
    if index != len(res) - 1:
        final_result = int(res[index + 1]) - step
    else:
        final_result = int(res[index - 1]) + step
    return final_result


def brain_progression_logic():
    game_rules = 'What number is missing in the progression?'
    answer_correct = []
    questions = []
    for i in range(ROUND_NUMBER):
        long_list = randint(5, 10)
        step = randint(1, 20)
        res_lst = []
        for j in range(long_list):
            if j == 0:
                res_lst.append(randint(1, 100))
            else:
                res_lst.append(res_lst[j - 1] + step)
        res_lst[randint(0, len(res_lst) - 1)] = '..'
        str_res_list = [str(res_lst[k]) for k in range(len(res_lst))]
        question = ' '.join(str_res_list)
        final_result = generation_result(question)
        answer_correct.append(final_result)
        questions.append(question)
    return engine(game_rules, questions, answer_correct)
