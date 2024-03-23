import prompt

from brain_games.cli import welcome_user


MAX_ROUND_QUANTITY = 3


def start_game(game):
    name = welcome_user()
    print(game.GAME_RULE)
    for round in range(MAX_ROUND_QUANTITY):
        question, correct_answer = game.get_game_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer != str(correct_answer):
            print((f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{correct_answer}'.\n"
                   f"Let's try again, {name}!"))
            round = 0
            break
        else:
            print('Correct!')
    if round == 2:
        print(f'Congratulations, {name}!')

