import prompt


def engine(question):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer in ['yes', 'no'] and type(question) == int:
        if (answer == 'yes' and question % 2 == 0) or (answer == 'no' and question % 2 != 0):
            return 'Correct!'
        else:
            if answer == 'yes' and question % 2 != 0:
                correct_answer = 'no'
                return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            else:
                correct_answer = 'yes'
                return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    elif type(question) == str and ('*' in question or '/' in question or '+' in question):
        lst = question.split()
        if lst[1] == '*':
            res = int(lst[0]) * int(lst[2])
        elif lst[1] == '-':
            res = int(lst[0]) - int(lst[2])
        else:
            res = int(lst[0]) + int(lst[2])
        if answer == str(res):
            return 'Correct!'
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{res}'."
    elif type(question) == str and len(question.split()) == 2:
        question_1 = [int(question.split()[0]), int(question.split()[1])]
        n = min(question_1)
        while n > 0:
            if question_1[0] % n == 0 and question_1[1] % n == 0:
                res = n
                break
            else:
                n -= 1
        if answer == str(res):
            return 'Correct!'
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{res}'."
    elif len(question.split()) >= 5:
        res = question.split()
        for k in range(len(res) - 1):
            if res[k] != '..' and res[k + 1] != '..':
                step = int(res[k + 1]) - int(res[k])
                break
        index = res.index('..')
        if index != len(res) - 1:
            final_result = int(res[index + 1]) - step
        else:
            final_result = int(res[index - 1]) + step
        if answer == str(final_result):
                return 'Correct!'
        else:
            return f"'{answer}' is wrong answer ;(. Correct answer was '{final_result}'."
    elif answer in ['yes', 'no'] and type(question) == str:
        numb = int(question)
        check_list = []
        if numb >= 2:
            for i in range(1, numb + 1):
                if numb % i == 0:
                    check_list.append(i)
        else:
            check_list = []
        if (len(check_list) == 2 and answer == 'yes') or (len(check_list) != 2 and answer == 'no'):
            return 'Correct!'
        else:
            if answer == 'yes' and len(check_list) != 2:
                correct_answer = 'no'
            else:
                correct_answer = 'yes'
            return f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
    