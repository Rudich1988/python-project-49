import prompt
from brain_games.cli import welcome_user


MAX_ROUND_QUANTITY = 3


def check_result(name, arg, answer=None, correct_answer=None):
    print((f"'{answer}' is wrong answer ;(. "
           f"Correct answer was '{correct_answer}'.\n"
           f"Let's try again, {name}!"))


def engine(rules, questions, answers_correct):
    print('Welcome to the Brain Games!')
    hello = welcome_user()
    print(rules)
    current_round = 0
    while current_round != MAX_ROUND_QUANTITY:
        print(f'Question: {questions[current_round]}')
        answer = prompt.string('Your answer: ')
        if answer != str(answers_correct[current_round]):
            return check_result(hello, 'error', answer,
                                answers_correct[current_round])
        else:
            print('Correct!')
        current_round += 1
    print(f'Congratulations, {hello}!')
