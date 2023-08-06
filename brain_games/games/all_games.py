import prompt
from brain_games.cli import welcome_user


ROUND_NUMBER = 3


def engine(rules, lst_questions, answers_correct):
    hello = welcome_user()
    print(rules)
    for i in range(ROUND_NUMBER):
        print(f'Question: {lst_questions[i]}')
        answer = prompt.string('Your answer: ')
        if answer != str(answers_correct[i]):
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{answers_correct[i]}'.\n"
                    f"Let's try again, {hello}"
                    )
            break
        else:
            print('Correct!')
    return f'Congratulations, {hello}!'
