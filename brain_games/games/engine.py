import prompt

from brain_games.cli import welcome_user

MAX_ROUND_QUANTITY = 3


def engine(generating_game_data, game_rules):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    current_round = 0
    print(game_rules)
    while current_round != MAX_ROUND_QUANTITY:
        question, correct_answer = generating_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print((f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'.\n"
                   f"Let's try again, {name}!"))
            break
        else:
            print('Correct!')
            current_round += 1
    if current_round == 3:
        print(f'Congratulations, {name}!')
