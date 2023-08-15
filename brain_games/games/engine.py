import prompt
from brain_games.cli import welcome_user


ROUND_NUMBER = 3


def check_result(name, arg, answer=None, correct_answer=None):
    if arg == 'error':
        print((f"'{answer}' is wrong answer ;(. "
               f"Correct answer was '{correct_answer}'.\n"
               f"Let's try again, {name}!"))
    else:
        print(f'Congratulations, {name}!')


def engine(rules, lst_questions, answers_correct):
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print(rules)
    for i in range(ROUND_NUMBER):
        print(f'Question: {lst_questions[i]}')
        answer = prompt.string('Your answer: ')
        if answer != str(answers_correct[i]):
            return check_result(hello, 'error', answer, answers_correct[i])
        else:
            print('Correct!')
    return check_result(hello, 'correct')
