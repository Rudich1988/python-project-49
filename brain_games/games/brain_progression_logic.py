from random import randint

GAME_RULES = 'What number is missing in the progression?'
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 20
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 100


def make_progression_element():
    length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    step = randint(MIN_STEP, MAX_STEP)
    progression_elements = []
    start = randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    for index in range(length):
        element = start + index * step
        progression_elements.append(str(element))
    return progression_elements


def get_game_data():
    progression_elements = make_progression_element()
    random_index = randint(0, len(progression_elements) - 1)
    correct_answer = progression_elements[random_index]
    progression_elements[random_index] = '..'
    question = ' '.join(progression_elements)
    return question, correct_answer
