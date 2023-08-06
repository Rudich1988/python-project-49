from brain_games.games.all_games import engine, ROUND_NUMBER
from random import randint


def brain_prime_logic():
    print('Welcome to the Brain Games!')
    game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    answer_correct = []
    questions = []
    for i in range(ROUND_NUMBER):
        lst = []
        numb = randint(1, 100)
        if numb >= 2:
            for j in range(1, numb + 1):
                if numb % j == 0:
                    lst.append(j)
        else:
            lst = []
        if len(lst) == 2:
            result = 'yes'
        else:
            result = 'no'
        questions.append(numb)
        answer_correct.append(result)
    return engine(game_rules, questions, answer_correct)
